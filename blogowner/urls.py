from django.conf.urls.defaults import patterns, url
from tbs.blogowner import views

urlpatterns = patterns('',
    #main
    url(r'^upload/$', views.upload),
    url(r'^upload/(\w+)/$', views.upload),
    url(r'^updatesites/$', views.updatesites),
    url(r'^updatesites/(\d+)/$', views.updatesites),
    url(r'^sponsor/$', views.sponsor),
    url(r'^register/$', views.register),
    url(r'^info/$', views.info),
    url(r'^$', views.home),
)