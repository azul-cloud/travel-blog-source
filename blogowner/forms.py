from django.forms import ModelForm
from django import forms
from tbs.travel.models import BlogSite, BlogEntry, BannerPic
from django.core.files.images import get_image_dimensions

class BlogSiteForm(ModelForm):
    site_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Website Name'}))
    url = forms.URLField(widget=forms.TextInput(attrs={'placeholder':'Website URL'}))
    #region = forms.CharField(widget=forms.Select(attrs={'placeholder':'Region'}))
    #category = forms.CharField(widget=forms.Select(attrs={'placeholder':'Category'}))
    twitter = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Twitter Handle'}))
    facebook = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Facebook Page'}))
    quick_info = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Quick Info'}))

    class Meta:
        model = BlogSite
        fields = ['site_name', 'url', 'region', 'category', 'twitter', 'facebook', 'quick_info']

class BlogEntryForm(ModelForm):
    class Meta:
        model = BlogEntry
        exclude = ('active_date', 'status')

class BannerPicForm(ModelForm):
    class Meta:
        model = BannerPic

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            raise forms.ValidationError("No image!")
        else:
            w, h = get_image_dimensions(image)
            if w < 800:
                raise forms.ValidationError("The image is %i pixel wide. It needs to be at least 800 pixels wide" %w)
            ratio = w/h
            if ratio < 3:
                raise forms.ValidationError("The image has a width/height ratio less than 3. The ratio of width to height needs to be at least 3.")
            return image