from django.db import models
from django.core.urlresolvers import reverse

from user.models import User, AbsTime

class Post(AbsTime):
	user = models.ForeignKey(User, null=True, verbose_name='User')

	title = models.CharField('Title', max_length=200, default='')
	text = models.TextField('Content', default='')	
	
	def get_absolute_url(self):
		return reverse('api-post:detail', kwargs = {'pk' : self.pk})

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created']


class Comment(AbsTime):
	user = models.ForeignKey(User, verbose_name='User')
	post = models.ForeignKey(Post, null=True, verbose_name='Post')
	text = models.CharField(verbose_name='Content', max_length=200, default='')

	
	def __str__(self):
		return self.text