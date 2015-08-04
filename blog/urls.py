from django.conf.urls import url
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    ######ACCOUTNS URL'S#######
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    #####HOME URL'S#####
    url(r'^home/$', views.post_list),
    url(r'^$', 'django.contrib.auth.views.login'),

    ######JOB URL'S######
    url(r'^job/new/$', views.job_new, name='job_new'),
    url(r'^job/list/$', views.job_list, name='job_list'),
    url(r'^job/(?P<pk>[0-9]+)/$', views.job_detail),

    ######EVENT URL'S######
    url(r'^event/new/$', views.event_new, name='event_new'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.event_detail),
    url(r'^event/(?P<pk>[0-9]+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^event/(?P<pk>[0-9]+)/remove/$', views.event_remove, name='event_remove'),

    #####ROSTER URL'S######
    url(r'^roster/$', views.schedule, name='schedule'),

    ######CALENDAR URL'S######
    url(r'^calendar/$', views.calendar_view, name='calendar_view'),

    #######POST URL'S######
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/list/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),

    ######COMMENT URL'S######
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),

    #######PBI/OPERATIONAL TASK URL'S#######
    url(r'^pbi/$', views.pbi_view, name='pbi'),
    url(r'^new/(?P<task_type>.*)/$', views.pbi_new, name='pbi_new'),
    url(r'^activity/(?P<pk>[0-9]+)/$', views.pbi_detail, name='pbi_detail'),
    url(r'^activity/(?P<pk>[0-9]+)/edit/$', views.pbi_edit, name='pbi_edit'),
    url(r'^activity/(?P<pk>[0-9]+)/remove/$', views.pbi_remove, name='pbi_remove'),
    url(r'^chart/$', views.pbi_chart, name='chart'),
    url(r'^operations/tracker$', views.operations_view, name='operations'),
    url(r'^activity/(?P<pk>[0-9]+)/update$', views.pbi_update, name='pbi_update'),

    ######TASK URL'S########
    url(r'^pbi/task/(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),
]