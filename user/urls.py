from django.conf.urls import url
from . import views


from django.contrib.auth.decorators import login_required as lr

urlpatterns=[
	url(r'^$', views.Index.as_view(), name="index"),
	url(r'^log_out/$',views.log_out, name="log_out"),
	url(r'^profile/$', lr(views.Profile.as_view()), name="profile"),

	url(r'^activate/$', views.Activate.as_view(), name="activate"),
	url(r'^recover/$', views.Recover.as_view(), name="recover"),
		
	
]