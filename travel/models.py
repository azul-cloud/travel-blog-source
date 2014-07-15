from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
#from django.core.exceptions import ValidationError
import os
import datetime

######upload paths######
def get_blog_image_path(instance, filename):
    return os.path.join('blogposts', filename)
def get_banner_image_path(instance, filename):
    if BannerPic.objects.all():
        max_banner_pic = BannerPic.objects.order_by("-id")[0]
        next_id = str(max_banner_pic.id + 1)
    else:
        next_id = "1"
    return os.path.join('region/bannerpic', next_id)

######Choice lists used in CharFields######
UPLOAD_STATUS_CHOICES = (
    ('N', 'New'),
    ('R', 'Rejected'),
    ('A', 'Accepted'),
)

SPONSOR_LEVEL_CHOICES = (
    ('Continent', 'Continent'),
    ('Country', 'Country'),
)

SPONSOR_TYPE_CHOICES = (
    ('NONE', 'None'),
    ('TOP', 'Top'),
    ('HIGH', 'Highlight'),
)

PRIMARY_LANGUAGE_CHOICES = (
    ('EN', 'English'),
    ('ES', 'Espanol'),
    ('DE', 'Deutsch'),
    ('FR', 'Francais'),
)

FEEDBACK_TOPIC_CHOICES = (
    ('BS', 'Blog Search'),
    ('BO', 'Blog Owner'),
    ('SPO', 'Sponsorship'),
    ('ACC', 'Account'),
    ('DES', 'Design'),
    ('GEN', 'General'),
)

FEEDBACK_TYPE_CHOICES = (
    ('ERR', 'Error/Bug'),
    ('SUG', 'Suggestion'),
    ('COM', 'Complaint'),
    ('QUE', 'Question'),
    ('OTH', 'Other')
)

FEEDBACK_STATUS_CHOICES = (
    ('S', 'Submitted'),
    ('P', 'Pending'),
    ('C', 'Closed'),
)

REGION_TYPE_CHOICES = (
    ('Continent', 'Continent'),
    ('Country', 'Country'),
)

CONTINENT_CHOICES = (
    ('world', 'The World'),
    ('southamerica', 'South America'),
    ('northamerica', 'North America'),
    ('europe', 'Europe'),
    ('asia', 'Asia'),
    ('africa', 'Africa'),
    ('oceania', 'Oceania'),
    ('continent', 'Continent'),
    ('none', 'None')
)

###### General ######
class Error(models.Model):
    error_desc = models.CharField(max_length="30")
    error_text = models.CharField(max_length="200")

class Error_Instance(models.Model):
    error_desc = models.CharField(max_length="200")
    error_date = models.DateField(db_index=True, auto_now_add=True)
    page = models.CharField(max_length="200")
    user = models.ForeignKey(User, null=True)


class HelpTopic(models.Model):
    question = models.CharField(max_length=100)
    question_order = models.IntegerField()
    answer = models.TextField()
    group = models.CharField(max_length=30)
    sub_group = models.CharField(max_length=30)
    active = models.BooleanField()

    class Meta:
        ordering = ['group', 'sub_group', 'question_order']

    def __unicode__(self):
        return '%s' % self.question

class Feedback(models.Model):
    user = models.ForeignKey(User)
    topic = models.CharField(max_length=30, choices=FEEDBACK_TOPIC_CHOICES)
    type = models.CharField(max_length=30, choices=FEEDBACK_TYPE_CHOICES)
    feedback = models.TextField()
    status = models.CharField(max_length=30, choices=FEEDBACK_STATUS_CHOICES, null=True, blank=True)
    submit_date = models.DateField(db_index=True, auto_now_add=True)

    class Meta:
        ordering = ['submit_date']

######Managers######
class RegionManager(models.Manager):
    def blog_site_count(self):
        blog_count = BlogSite.objects.filter(region=self).count()
        return blog_count

######Core Models######
class Region(models.Model):
    value = models.CharField(max_length=50)
    display_value = models.CharField(max_length=60)
    continent = models.CharField(max_length=50, choices=CONTINENT_CHOICES, default='world')
    active = models.BooleanField()
    views = models.IntegerField(editable=False, null=True, blank=True, default=0)
    blog_entry_pay = models.BooleanField(default=False)
    banner_pic_pay = models.BooleanField(default=False)
    region_type = models.CharField(max_length=30, choices=REGION_TYPE_CHOICES, default='Country')

    def __unicode__(self):
        return '%s' % self.display_value

    def blog_site_count(self):
        blog_count = BlogSite.objects.filter(region=self, active=True).count()
        return blog_count

    def blog_continent_count(self):
        blog_continent_count = BlogSite.objects.filter(region__continent=self.value, active=True).count()
        return blog_continent_count

    class Meta:
        ordering = ['display_value']

class Category(models.Model):
    value = models.CharField(max_length=50)
    display_value = models.CharField(max_length=60)
    active = models.BooleanField()
    views = models.IntegerField(editable=False, null=True, blank=True, default=0)
    banner_pic_pay = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.display_value

    def blog_site_count(self):
        blog_count = BlogSite.objects.filter(category=self, active=True).count()
        return blog_count

    class Meta:
        ordering = ['display_value']

class SponsorLevel(models.Model):
    sponsor_level = models.CharField(max_length=30, choices=SPONSOR_LEVEL_CHOICES)

    def __unicode__(self):
        return '%s' % self.sponsor_level

class SponsorType(models.Model):
    sponsor_type = models.CharField(max_length=30, choices=SPONSOR_TYPE_CHOICES)

    def __unicode__(self):
        return '%s' % self.sponsor_type

class BlogSite(models.Model):
    blog_owner = models.ForeignKey(User)
    site_name = models.CharField(max_length=300)
    region = models.ForeignKey(Region, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    #region = models.ManyToManyField('Region', blank=True, null=True)
    url = models.URLField(max_length=200)
    sponsor_type = models.CharField(max_length=30, choices=SPONSOR_TYPE_CHOICES, default="NONE")
    sponsor_begin_date = models.DateField(null=True, blank=True)
    sponsor_end_date = models.DateField(null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    primary_language = models.CharField(max_length=50, choices=PRIMARY_LANGUAGE_CHOICES, blank=True)
    twitter = models.CharField(max_length=20, blank=True)
    #removed twitter-id because not viable for users to find their Twitter Data ID --AWW 2013209
    #twitter_id = models.CharField(max_length=30, null=True, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    quick_info = models.CharField(max_length=300, blank=True)
    active = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=UPLOAD_STATUS_CHOICES, default="N")

    #def clean(self, *args, **kwargs):
    #    if self.region.count() > 3:
    #        raise ValidationError("You can't assign more than three regions")
    #    super(BlogSite, self).clean(*args, **kwargs)

    class Meta:
        ordering = ['site_name']

    def __unicode__(self):
        return '%s' % self.site_name

    #get the average rating for a blogsite
    def rating_avg(self):
        rating_dict = BlogSiteReview.objects.filter(blog_site=self).aggregate(Avg('review_rating'))
        rating_avg = rating_dict.get('review_rating__avg')
        if rating_avg:
            #round to nearest int
            return int(round(rating_avg) - .5) + (rating_avg > 0)
        else:
            #no ratings
            return 0

    def active_sponsor(self):
        today = datetime.datetime.now()
        active = BlogSite.objects.exclude(sponsor_type = "NONE").filter(
            id=self.id, sponsor_end_date__gte=today, sponsor_begin_date__lte=today)

        if active:
            return True
        else:
            return False

class BlogEntry(models.Model):
    title = models.CharField(max_length=50, unique=True)
    headline = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(User)
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=get_blog_image_path)
    image_title = models.CharField(max_length=100, blank=True)
    blog_site = models.ForeignKey(BlogSite, null=True, blank=True)
    region = models.ForeignKey(Region, null=True, blank=True)
    active = models.BooleanField()
    active_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=UPLOAD_STATUS_CHOICES, default="N")
    views = models.IntegerField(editable=False, default=0)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['-post_date']

class BannerPic(models.Model):
    title = models.CharField(max_length=100)
    image =  models.ImageField(upload_to=get_banner_image_path)
    user = models.ForeignKey(User)
    region = models.ForeignKey(Region, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    active = models.BooleanField(default=False)
    active_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=UPLOAD_STATUS_CHOICES, default="N")
    url = models.URLField(max_length=100)

    def __unicode__(self):
        return '%s' % self.title

class BlogSiteReview(models.Model):
    blog_site = models.ForeignKey(BlogSite)
    user = models.ForeignKey(User)
    review_rating = models.IntegerField()
    sponsor_type = models.CharField(max_length=30, choices=SPONSOR_TYPE_CHOICES, default="NONE")
    review_date = models.DateField(auto_now_add=True, db_index=True)

    def __unicode__(self):
        return '%s' % self.blog_site

    class Meta:
        ordering = ['-review_date']