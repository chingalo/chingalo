from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^createpoll/$', views.create_poll, name='create_poll'),
    url(r'^(?P<poll_id>\d+)/delete/$', views.delete, name= 'delete'),    
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
)
