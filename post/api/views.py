from rest_framework import generics
from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import (
	redirect, 
	reverse, 
	get_object_or_404)

from post.models import Post

from . import serializer, pagination


class PostListAPIView(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = serializer.PostListSerializer

	pagination_class = pagination.CustomPagination


class PostDetailApiView(generics.RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = serializer.PostDetailSerializer


class PostUpadteApiView(generics.UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = serializer.PostSerializer

	def get(self, request, *args, **kwargs):
		object = self.queryset.get(pk=kwargs['pk'])
		serializer = self.serializer_class(object)

		return Response(serializer.data)


class PostDeleteApiView(generics.DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = serializer.PostSerializer

	def get(self, request, *args, **kwargs):
		object = self.queryset.get(pk=kwargs['pk'])
		serializer = self.serializer_class(object)
		return Response(serializer.data)


class PostCreateApiView(generics.CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = serializer.PostCreateSerializer

	def post(self, request, *args, **kwargs):

		post = Post()
		post.user = request.user
		post.title = request.POST.get('title')
		post.text = request.POST.get('text')
		post.save()

		return redirect(reverse('api-post:detail', kwargs={'pk' : post.pk}))