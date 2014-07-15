from django.conf.urls.defaults import patterns, url
from tbs.blogsearch import views

urlpatterns = patterns('',
    #main
    url(r'^$', views.home),
    url(r'^(?P<pk>region)/(\w+)/$', views.search),
    url(r'^(category)/(\w+)/$', views.search),
    url(r'^(text)/(.+)/$', views.search),
    url(r'^setrating/$', views.setrating),
    url(r'^blog/(\d+)/', views.blog),
    url(r'^blogsiteclick/$', views.blogsiteclick),
    url(r'^bannerpicclick/$', views.bannerpicclick),
)