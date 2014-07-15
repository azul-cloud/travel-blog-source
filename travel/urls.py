from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout, password_change, password_reset_done

from tbsdev.travel import views

urlpatterns = patterns('',
    #main
    url(r'^$', views.home),
    url(r'^contact/$', views.contact),
    url(r'^about/$', views.about),
    url(r'^help/$', views.help),
    url(r'^help/(\w+)/$', views.help),
    url(r'^feedback/$', views.feedback),
    url(r'^testing/$', views.testing),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name="content/robots.txt")),

    #auth
    (r'^accounts/login/$',  login),
    (r'^accounts/password/$',  password_change,
        {'template_name': 'registration/passwordchange.html',
        'post_change_redirect': '/accounts/passwordchangedone/'}),
    (r'^accounts/logout/$', logout,
        {'next_page': '/'}),
    (r'^accounts/register/$', views.register),
    (r'^accounts/passwordchangedone/$', password_reset_done,
        {'template_name': 'registration/passwordchangedone.html'}),
    (r'^accounts/profile/$', views.updateprofile),
    (r'^accounts/verifyemail/(\S+)/$', views.verifyemail)
)