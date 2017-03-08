from django.conf.urls import url, include
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index),
    url(r'^api/post/', include('post.api.urls', namespace='api-post')),
    url(r'^api/user/', include('user.api.urls', namespace='api-user')),
]
