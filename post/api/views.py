from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import (
		AllowAny,
		IsAuthenticated,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	)
from .permissions import IsOwnerOrReadOnly

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

	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def get(self, request, *args, **kwargs):
		object = self.queryset.get(pk=kwargs['pk'])
		serializer = self.serializer_class(object)
		
		return Response(serializer.data)

		


class PostDeleteApiView(generics.DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = serializer.PostSerializer

	permission_classes = [IsOwnerOrReadOnly]

	def get(self, request, *args, **kwargs):
		object = self.queryset.get(pk=kwargs['pk'])
		serializer = self.serializer_class(object)
		return Response(serializer.data)


class PostCreateApiView(generics.CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = serializer.PostCreateSerializer
	permission_classes = [IsAuthenticated]


	def post(self, request, *args, **kwargs):

		post = Post()
		post.user = request.user
		post.title = request.POST.get('title')
		post.text = request.POST.get('text')
		post.save()

		return redirect(reverse('api-post:detail', kwargs={'pk' : post.pk}))

class CommentCreateApiView(generics.CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = serializer.CommentCreateSerializer
	permission_classes = [IsAuthenticated]

	def get(self, request, *args, **kwargs):
		object = self.queryset.get(pk=kwargs['pk'])
		serializer_local = serializer.PostdetailSerializer(object)
		return Response(serializer_local.data)

	def post(self, request, *args, **kwargs):
		object = self.queryset.get(pk=kwargs['pk'])
		object.comment_set.create(
				text=request.POST.get('text'),
				user=request.user
			)
		return redirect(reverse('api-post:addcomment', kwargs={'pk' : kwargs['pk']}))