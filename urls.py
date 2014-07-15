from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blogsearch/', include('tbsdev.blogsearch.urls')),
    url(r'^blogowner/', include('tbsdev.blogowner.urls')),
    url(r'^reports/', include('tbsdev.reports.urls')),
    url(r'^internal/', include('tbsdev.internal.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),

    #travel needs to be last or it will handle all URLs
    url(r'^', include('tbsdev.travel.urls')),
)



