from django.conf.urls import url, include
from . import views

from django.contrib.auth.decorators import login_required as lr

urlpatterns = [
	url(r'^$', views.PostListAPIView.as_view(), name='listing'),
	url(r'^create/$', views.PostCreateApiView.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/$', views.PostDetailApiView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/edit/$', views.PostUpadteApiView.as_view(), name='edit'),
	url(r'^(?P<pk>\d+)/delete/$', views.PostDeleteApiView.as_view(), name='delete'),

	url(r'^(?P<pk>\d+)/addcomment/$', views.CommentCreateApiView.as_view(), name='addcomment'),

	
]