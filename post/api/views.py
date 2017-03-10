from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import mixins

from django.shortcuts import redirect, reverse, get_object_or_404
from post.models import Post, Comment
from . import serializer, pagination

from user.models import User


class PostListAPIView(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = serializer.PostListSerializer

	pagination_class = pagination.CustomPagination

class PostCreateApiView(generics.CreateAPIView):
	model = Post
	serializer_class = serializer.PostCreateSerializer
	# permission_classes = [IsAuthenticated]


	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class PostDetailApiView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
	model = Post
	serializer_class = serializer.PostDetailSerializer

	def get_object(self):
		obj = get_object_or_404(self.model, pk=self.kwargs['pk'])
		return obj

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class CommentListApiView(mixins.CreateModelMixin, generics.ListAPIView):
	model = Comment
	serializer_class = serializer.CommentDetailSerializer
	# permission_classes = [IsAuthenticated]

	def get_queryset(self):
		post = Post.objects.get(pk=self.kwargs['pk'])
		return post.comment_set

	def perform_create(self, serializer):
		post = Post.objects.get(pk=self.kwargs['pk'])
		serializer.save(user=self.request.user, post=post)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)