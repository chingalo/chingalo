from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='view_all_polls'),
    url(r'^createpoll/$', views.create_poll, name='create_poll'),
    url(r'^views/$', views.view_all, name='view_all'),
    url(r'^(?P<poll_id>\d+)/delete/$', views.delete, name= 'delete_poll'),   
    url(r'^createchoice/$',views.create_choice, name='create_choice'),
    url(r'^vote/$', views.vote, name='vote'), 
    url(r'^(?P<poll_id>\d+)/edit/$', views.edit_poll, name='edit_poll'),
    url(r'^(?P<poll_id>\d+)/warning/$', views.warning, name='warning'),
       
)
