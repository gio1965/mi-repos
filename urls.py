from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/edit/(?P<matricula_id>\d+)/$', views.post_edit, name='post_edit'),
]