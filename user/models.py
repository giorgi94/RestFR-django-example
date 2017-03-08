from django.db import models
from django.shortcuts import reverse
# from django.core.mail import EmailMessage
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .helpers import unique_token, generate_token

class AbsTime(models.Model):
	created = models.DateTimeField('Created', auto_now_add=True, null=True)
	updated = models.DateTimeField('Updated', auto_now=True, null=True)

	class Meta:
		abstract = True

class AccountManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		if not email:
			raise ValueError('The Email Exists')

		if not kwargs.get('first_name'):
			raise ValueError('First Name is required')

		if not kwargs.get('last_name'):
			raise ValueError('Last Name is required')

		user = self.model(
			email=self.normalize_email(email),
			first_name=kwargs.get('first_name'),
			last_name=kwargs.get('last_name')
		)

		user.set_password(password)
		user.save()

		return user

	def create_superuser(self, email, password, **kwargs):
		user = self.create_user(email, password, **kwargs)
		user.is_staff = True
		user.is_admin = True
		user.is_active = True
		user.is_superuser = True
		user.save()

		return user


class User(AbstractBaseUser, PermissionsMixin, AbsTime):
	token = models.CharField('Tokens', max_length=100, blank=True, default='')

	email = models.EmailField(verbose_name='E-Mail', unique=True)
	first_name = models.CharField(verbose_name='First Name', max_length=40, default='')
	last_name = models.CharField(verbose_name='Last Name', max_length=40, default='')
	
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	
	objects = AccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def __str__(self):
		return self.email

	def set_new_token(self):
		tokens = [u.token for u in User.objects.all()]			
		self.token = unique_token(generate_token(), tokens)
		self.save()

	def get_full_name(self):
		if self.first_name != '' and self.last_name != '':
			return ' '.join([self.first_name, self.last_name])
		return self.email

	def get_short_name(self):
		return self.first_name


	'''
	def send_activation_email(self subj, body HTTP_HOST):
		try:
			ACT_LINK = reverse("user:activate") + '?token=' + self.token
			ACT_LINK = "http://" + HTTP_HOST + ACT_LINK

			msg = EmailMessage(
						ACT_MES_SUBJ,
						ACT_MES_BODY,
						settings.EMAIL_HOST_USER,
						(self.email,)
					)

			msg.content_subtype = "html"
			msg.send()

		except Exception as ge:
			print('Email was not sent')
		'''



@receiver(post_save, sender=User)
def p_save(sender, **kwargs):
	instance = kwargs.get("instance")	
	if kwargs['created']:
		instance.set_new_token()