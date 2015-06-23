from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^job/new/$', views.job_new, name='job_new'),
    url(r'^job/list/$', views.job_list),
    url(r'^job/(?P<pk>[0-9]+)/$', views.job_detail),
]