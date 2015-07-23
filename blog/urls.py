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
    url(r'^event/new/$', views.event_new, name='event_new'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.event_detail),
    url(r'^event/(?P<pk>[0-9]+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^event/(?P<pk>[0-9]+)/remove/$', views.event_remove, name='event_remove'),
    url(r'^job/new/$', views.job_new, name='job_new'),
    url(r'^job/list/$', views.job_list, name='job_list'),
    url(r'^calendar/$', views.calendar_view, name='calendar_view'),
    url(r'^roster/$', views.schedule, name='schedule'),
    url(r'^job/(?P<pk>[0-9]+)/$', views.job_detail),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]