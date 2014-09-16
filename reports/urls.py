from django.conf.urls.defaults import patterns, url
from tbs.reports import views

urlpatterns = patterns('',
    #main
    url(r'^$', views.home),
    url(r'^(myblog)/$', views.myblog),
    url(r'^(myblog)/(\d+)/$', views.myblog),
    url(r'^(allblogs)/$', views.allblogs),
    url(r'^(blogsearch)/$', views.blogsearch),
    url(r'^(admin)/$', views.admin),
)