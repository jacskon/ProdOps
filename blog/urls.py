from django.conf.urls import url
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^home/$', views.index),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^post/list/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^job/new/$', views.job_new, name='job_new'),
    url(r'^job/list/$', views.job_list, name='job_list'),
    url(r'^job/(?P<pk>[0-9]+)/$', views.job_detail),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
]