from django.db import models
from tbs.travel.models import BlogSite

SPONSOR_TYPE_CHOICES = (
    ('NONE', 'None'),
    ('TOP', 'Top'),
    ('HIGH', 'Highlight'),
)

ACTION_TYPE_CHOICES = (
    ('NONE', 'None'),
    ('DELETE', 'Delete'),
    ('ADD', 'Add'),
    ('CHANGE', 'Change')
)

# Create your models here.
class SponsorHistory(models.Model):
    blog_site = models.ForeignKey(BlogSite)
    action_date = models.DateField(auto_now_add=True)
    action_type =  models.CharField(max_length=30, choices=ACTION_TYPE_CHOICES, default="NONE")
    old_sponsor_type = models.CharField(max_length=30, choices=SPONSOR_TYPE_CHOICES, default="NONE")
    old_sponsor_begin_date = models.DateField(null=True, blank=True)
    old_sponsor_end_date = models.DateField(null=True, blank=True)
    new_sponsor_type = models.CharField(max_length=30, choices=SPONSOR_TYPE_CHOICES, default="NONE")
    new_sponsor_begin_date = models.DateField(null=True, blank=True)
    new_sponsor_end_date = models.DateField(null=True, blank=True)
