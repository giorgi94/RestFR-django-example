from rest_framework import serializers
from django.utils import timezone
from user.models import User
from post.models import Post

from datetime import datetime

from django.shortcuts import redirect, reverse


user_datail_url = serializers.HyperlinkedIdentityField(
				view_name='api-user:detail',
				lookup_field='pk'
			)

user_edit_url = serializers.HyperlinkedIdentityField(
				view_name='api-user:edit',
				lookup_field='pk'
			)

user_delete_url = serializers.HyperlinkedIdentityField(
				view_name='api-user:delete',
				lookup_field='pk'
			)


class UserListSerializer(serializers.ModelSerializer):
	url = user_datail_url

	class Meta:
		model = User
		fields = [
				'url',
				'pk',
				'email',
			]


class UserListSerializer(serializers.ModelSerializer):
	url = user_datail_url

	class Meta:
		model = User
		fields = [
				'url',
				'email',
			]



class UserDetailSerializer(serializers.ModelSerializer):
	edit = user_edit_url
	delete = user_delete_url


	created = serializers.SerializerMethodField()
	updated = serializers.SerializerMethodField()

	posts = serializers.SerializerMethodField()


	def get_created(self, obj):
		return timezone.localtime(obj.created).strftime("%d/%m/%Y %H:%M:%S")

	def get_updated(self, obj):
		return timezone.localtime(obj.updated).strftime("%d/%m/%Y %H:%M:%S")

	def get_posts(self, obj):
		c_qs = obj.post_set.all()
		posts = PostSerializer(c_qs, many=True).data
		return posts

	class Meta:
		model = User
		fields = [
				'edit',
				'delete',
				'pk',
				'email',
				'created',
				'updated',
				'posts',
			]




class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
				'email',
			]



class PostLinkSerializer(serializers.HyperlinkedModelSerializer):

	post = serializers.SerializerMethodField('get_post_link')

	def get_post_link(self, obj):

		print('...............')
		print(obj)

		return reverse('api-post:detail', kwargs={'pk', self.context['pk']})

	class Meta:
		model = Post


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = [
				'pk',
				'title',
				'text',
			]


