from tbs.travel.models import BlogSite, BlogEntry, BannerPic
from django.db import models
from django.contrib.auth.models import User

BLOGSITE_CLICK_ORIGIN_CHOICES = (
    ('SEARCH', 'Search'),
    ('POST', 'Post')
)

SPONSOR_TYPE_CHOICES = (
    ('NONE', 'None'),
    ('TOP', 'Top'),
    ('HIGH', 'Highlight'),
    ('BLOG', 'Blog')
)

class BlogEntryClick(models.Model):
    blog_entry = models.ForeignKey(BlogEntry, null=True, blank=True)
    click_date = models.DateField(auto_now_add=True)
    user_name = models.ForeignKey(User)

class BlogSiteClick(models.Model):
    blog_site = models.ForeignKey(BlogSite, null=True, blank=True)
    click_date = models.DateField(auto_now_add=True)
    sponsor_type = models.CharField(max_length=30, choices=SPONSOR_TYPE_CHOICES, default="NONE")
    origin = models.CharField(max_length=50, default="SEARCH", choices=BLOGSITE_CLICK_ORIGIN_CHOICES)

    def __unicode__(self):
        return '%s' % self.origin

class BannerPicClick(models.Model):
    banner_pic = models.ForeignKey(BannerPic, null=True, blank=True, editable=False)
    click_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.banner_pic.title