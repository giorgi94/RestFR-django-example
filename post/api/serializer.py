from rest_framework import serializers
from django.utils import timezone

from post.models import Post, Comment

from django.shortcuts import redirect

from datetime import datetime



post_datail_url = serializers.HyperlinkedIdentityField(
				view_name='api-post:detail',
				lookup_field='pk'
			)

post_edit_url = serializers.HyperlinkedIdentityField(
				view_name='api-post:edit',
				lookup_field='pk'
			)
post_delete_url = serializers.HyperlinkedIdentityField(
				view_name='api-post:delete',
				lookup_field='pk'
			)

class PostListSerializer(serializers.ModelSerializer):
	url = post_datail_url

	user = serializers.SerializerMethodField()

	def get_user(self, obj):
		return obj.user.email

	class Meta:
		model = Post
		fields = [
				'url',
				'user',
				'title',
			]



class PostDetailSerializer(serializers.ModelSerializer):
	edit = post_edit_url
	delete = post_delete_url

	user = serializers.SerializerMethodField()

	created = serializers.SerializerMethodField()
	updated = serializers.SerializerMethodField()

	comments = serializers.SerializerMethodField()

	def get_user(self, obj):
		return obj.user.email

	def get_created(self, obj):
		return timezone.localtime(obj.created).strftime("%d/%m/%Y %H:%M:%S")

	def get_updated(self, obj):
		return timezone.localtime(obj.updated).strftime("%d/%m/%Y %H:%M:%S")

	def get_comments(self, obj):
		c_qs = obj.comment_set.all()
		comments = CommentSerializer(c_qs, many=True).data
		return comments

	class Meta:
		model = Post
		fields = [
				'edit',
				'delete',
				'pk',
				'user',
				'title',
				'text',
				'created',
				'updated',
				'comments',
			]




class PostSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Post
		fields = [
				'title',
				'text',
			]



class PostCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = [
				'title',
				'text',
			]

class CommentSerializer(serializers.ModelSerializer):
	user = serializers.SerializerMethodField()

	def get_user(self, obj):
		return obj.auth.email

	class Meta:
		model = Comment
		fields = [
				'user',
				'text',
			]