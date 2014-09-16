from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #blogsearch
    url(r'^blogsearch/', include('tbs.blogsearch.urls')),

    #blogowner
    url(r'^blogowner/', include('tbs.blogowner.urls')),

    #reports
    url(r'^reports/', include('tbs.reports.urls')),

    #internal
    url(r'^internal/', include('tbs.internal.urls')),

    #admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #travel needs to be last or it will handle all URLs
    url(r'^', include('tbs.travel.urls')),

    #social auth
    url(r'', include('social_auth.urls')),
)
