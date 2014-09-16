from django.conf.urls.defaults import patterns, url
from tbs.internal import views

urlpatterns = patterns('',
    #main
    url(r'^$', views.home),
    url(r'^cleansponsors/$', views.cleansponsors),
    url(r'^sponsorhistory/$', views.sponsorhistory),
    url(r'^managesponsors/$', views.managesponsors),
    url(r'^bannerpics/$', views.bannerpics),
    url(r'^bannerpics/(\d+)/$', views.bannerpics),
    url(r'^blogentries/$', views.blogentries),
    url(r'^blogentries/(\d+)/$', views.blogentries),
    url(r'^feedback/$', views.feedback),
    url(r'^feedback/(\d+)/$', views.feedback),
    url(r'^blogsites/$', views.blogsites),
    url(r'^blogsites/(\d+)/$', views.blogsites),
)