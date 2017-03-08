from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from django.shortcuts import (
	redirect, 
	reverse, 
	get_object_or_404)

from django.contrib.auth import (
	authenticate, 
	login, 
	logout)

from user.models import User

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

class UserLoginApiView(APIView):
	serializer_class = serializer.UserLoginSerializer


	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = self.serializer_class(data=data)

		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			user=authenticate(
							email=new_data.get('email'), 
							password=new_data.get('password'))
			if user:
				login(request, user)
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)