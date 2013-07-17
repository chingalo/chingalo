from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='view all polls'),
    url(r'^createpoll/$', views.create_poll, name='create_poll'),
    url(r'^(?P<poll_id>\d+)/delete/$', views.delete, name= 'delete a poll'),    
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='choice of given poll'),
    url(r'^createchoice/$',views.create_choice, name=' create choice for a given poll'),
)
