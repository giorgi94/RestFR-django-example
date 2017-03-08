from django.conf.urls import url, include
from . import views

from django.contrib.auth.decorators import login_required as lr

urlpatterns = [
	url(r'^$', views.UserListAPIView.as_view(), name='listing'),
	# url(r'^create/$', views.UserCreateApiView.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/$', views.UserDetailApiView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/edit/$', views.UserUpadteApiView.as_view(), name='edit'),
	url(r'^(?P<pk>\d+)/delete/$', views.UserDeleteApiView.as_view(), name='delete'),
	
]