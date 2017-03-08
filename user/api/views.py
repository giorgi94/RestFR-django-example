from rest_framework import generics
from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import (
	redirect, 
	reverse, 
	get_object_or_404)

from post.models import User

from . import serializer, pagination


class UserListAPIView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = serializer.UserListSerializer

	pagination_class = pagination.CustomPagination


class UserDetailApiView(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = serializer.UserDetailSerializer


class UserUpadteApiView(generics.UpdateAPIView):
	queryset = User.objects.all()
	serializer_class = serializer.UserSerializer

	def get(self, request, *args, **kwargs):
		object = self.queryset.get(pk=kwargs['pk'])
		serializer = self.serializer_class(object)

		return Response(serializer.data)


class UserDeleteApiView(generics.DestroyAPIView):
	queryset = User.objects.all()
	serializer_class = serializer.UserSerializer

	def get(self, request, *args, **kwargs):
		object = self.queryset.get(pk=kwargs['pk'])
		serializer = self.serializer_class(object)
		return Response(serializer.data)


'''
class UserCreateApiView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = serializer.UserCreateSerializer

	def post(self, request, *args, **kwargs):

		user = User()
		post.user = request.user
		post.title = request.POST.get('title')
		post.text = request.POST.get('text')
		post.save()

		return redirect(reverse('api-post:detail', kwargs={'pk' : post.pk}))
'''