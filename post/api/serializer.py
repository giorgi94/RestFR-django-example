from datetime import datetime
from django.utils import timezone
from django.shortcuts import redirect

from rest_framework import serializers
from post.models import Post, Comment

post_datail_url = serializers.HyperlinkedIdentityField(
						view_name='api-post:detail',
						lookup_field='pk'
					)

class PostCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = [
				'title',
				'text',
			]

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
		comments = CommentListSerializer(c_qs, many=True).data
		return comments

	class Meta:
		model = Post
		fields = [
				'pk',
				'user',
				'title',
				'text',
				'comments',
				'created',
				'updated',
			]
		read_only_fields = [
				'pk',
				'user',
				'created',
				'updated',
			]


class CommentListSerializer(serializers.ModelSerializer):
	user = serializers.SerializerMethodField()

	def get_user(self, obj):
		return obj.user.email

	class Meta:
		model = Comment
		fields = [
				'user',
				'text',
			]
		read_only_fields = [
				'user',
			]

class CommentDetailSerializer(serializers.ModelSerializer):
	user = serializers.SerializerMethodField()

	created = serializers.SerializerMethodField()
	updated = serializers.SerializerMethodField()

	def get_user(self, obj):
		return obj.user.email

	def get_created(self, obj):
		return timezone.localtime(obj.created).strftime("%d/%m/%Y %H:%M:%S")

	def get_updated(self, obj):
		return timezone.localtime(obj.updated).strftime("%d/%m/%Y %H:%M:%S")

	class Meta:
		model = Comment
		fields = [
				'pk',
				'user',
				'text',
				'created',
				'updated',
			]
		read_only_fields = [
				'pk',
				'user',
				'created',
				'updated',
			]