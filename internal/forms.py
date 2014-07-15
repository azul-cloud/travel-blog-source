from django.forms import ModelForm
from django import forms
from tbs.travel.models import BannerPic, BlogEntry, BlogSite, Feedback

class BannerPicForm(ModelForm):
    class Meta:
        model = BannerPic
        exclude = ('image', 'url', 'user')

class BlogEntryForm(ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['status', 'region', 'active_date', 'active']

class BlogSiteForm(ModelForm):
    quick_info = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = BlogSite
        fields = ['site_name', 'quick_info', 'category', 'region', 'url', 'twitter', 'facebook', 'status', 'active']

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['user', 'status']