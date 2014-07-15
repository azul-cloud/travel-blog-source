from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from django.db.models import Count
from django.conf import settings
#from django.db.models.signals import pre_save, post_save
#from django import forms
from tbs.travel.models import BlogSite, BannerPic, BlogEntry, Feedback
from tbs.internal.forms import BannerPicForm, BlogEntryForm, BlogSiteForm, FeedbackForm
import datetime

#To show the home page for the internal site
@staff_member_required
def home(request):
    new_blog_sites = BlogSite.objects.filter(status="N")
    new_blog_entries = BlogEntry.objects.filter(status="N")
    new_banner_pics = BannerPic.objects.filter(status="N")
    new_feedback = Feedback.objects.filter(status="N")

    return render(request, 'internalcontent/home.html',
        {'newblogsites':new_blog_sites, 'newblogentries':new_blog_entries,
        'newbannerpics':new_banner_pics, 'newfeedback':new_feedback})

#To update the BlogSite model to reflect the correct sponsorship
@staff_member_required
def cleansponsors(request):
    sponsored_blog_site = BlogSite.objects.exclude(sponsor_type = "NONE")
    today = datetime.date.today()
    expired = []

    #for the list of sponsored sites, if they are expired, fix them
    for blog_site in sponsored_blog_site:
        if blog_site.sponsor_end_date < today:
            expired.append(blog_site)
            blog_site.sponsor_type = "NONE"
            blog_site.sponsor_begin_date = None
            blog_site.sponsor_end_date = None
            blog_site.save()

    return render(request, 'internalcontent/cleansponsors.html',
        {'all':sponsored_blog_site, 'expired':expired})

@staff_member_required
def sponsorhistory(request):
    return render(request, 'internalcontent/sponsorhistory.html')

@staff_member_required
def managesponsors(request):
    return render(request, 'internalcontent/managesponsors.html')

#Banner Pic Review and Management
@staff_member_required
def bannerpics(request, id=None):
    all_banner_pics = BannerPic.objects.all()

    #get list of new banner pics to review
    new = all_banner_pics.filter(status="N")

    if id:
        if id:
            single_pic = BannerPic.objects.get(id=id)

        #get active to determine whether to send email
        if not single_pic.active:
            prev_inactive = True
        else:
            prev_inactive = False
    else:
        single_pic = None
        prev_inactive = False

    #get list of regions with multiple active banner pics
    #this just returns the value set, not the BannerPic objects
    multiple_active_regions = all_banner_pics.filter(active=True) \
        .values('region__display_value').annotate(region_count=Count('region'))\
        .filter(region_count__gt=1)

    multiple_active_categories = all_banner_pics.filter(active=True) \
        .values('category__display_value').annotate(category_count=Count('category'))\
        .filter(category_count__gt=1)

    if request.method == 'POST':
        form = BannerPicForm(request.POST, request.FILES, instance=single_pic)
        if form.is_valid():
            #set currently active to inactive if new active.
            #Possible to have multiples.
            region_pic_active = BannerPic.objects.filter(region=single_pic.region, active=True)

            for pic in region_pic_active:
                pic.active = False
                pic.save()

            #save new active
            form.save()

            #if it was inactive and now active, send an email
            if prev_inactive and single_pic.active:
                msg = EmailMessage('Travel Blog Source - Banner Picture Approved',
                    get_template('emails/bannerpicactive.html').render(
                        Context({
                            'bannerpic': single_pic,
                            'webURLroot' : settings.WEB_URL_ROOT
                        })
                    ),
                    settings.EMAIL_HOST_USER,
                    [single_pic.user.email, 'admin@travelblogsource.com']
                )
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()
    else:
        if single_pic:
            form = BannerPicForm(
                initial={
                    'title': single_pic.title,
                    'active': single_pic.active,
                    'active_date': single_pic.active_date,
                    'status': single_pic.status,
                    'region': single_pic.region,
                    'category': single_pic.category})
        else:
            form = BannerPicForm()

    return render(request, 'internalcontent/bannerpics.html',
        {'multiple_ids':multiple_active_regions, 'new':new, 'form':form,
        'singlepic':single_pic})

#get blog entries to perform management tasks
def blogentries(request, id=None):
    all_blog_entries = BlogEntry.objects.all()
    new_blog_entries = all_blog_entries.filter(status="N")

    #get blog from parameter passed in
    if id:
        single_entry = all_blog_entries.get(id=id)
        #had to comment this out for now because people can submit without region and causes error
        #blog_entry_pay = single_entry.region.blog_entry_pay
        blog_entry_pay = None

        #get active to determine whether to send email
        if not single_entry.active:
            prev_inactive = True
        else:
            prev_inactive = False

        #get last active for a region
        last_active = all_blog_entries.filter(region=single_entry.region).order_by("-active_date")[0]
    else:
        single_entry = None
        blog_entry_pay = None
        last_active = None
        prev_inactive = False

    if request.method == 'POST':
        form = BlogEntryForm(request.POST, instance=single_entry)
        if form.is_valid():
            form.save()

            #if it was inactive and now active, send an email
            if prev_inactive and single_entry.active:
                msg = EmailMessage('Travel Blog Source - Blog Entry Approved',
                    get_template('emails/blogentryactive.html').render(
                        Context({
                            'blogentry': single_entry,
                            'webURLroot' : settings.WEB_URL_ROOT
                        })
                    ),
                    settings.EMAIL_HOST_USER,
                    [single_entry.blog_site.blog_owner.email, 'admin@travelblogsource.com']
                )
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()
    else:
        if id:
            form = BlogEntryForm(initial={
                'title': single_entry.title,
                'active': single_entry.active,
                'active_date': single_entry.active_date,
                'region': single_entry.region})
            form.fields['region'].widget.attrs['readonly'] = True
        else:
            form = BlogEntryForm()

    return render(request, 'internalcontent/blogentries.html',
        {'newblogentries':new_blog_entries, 'singleentry':single_entry,
        'form':form, 'blogentrypay':blog_entry_pay, 'lastactive':last_active})

def feedback(request, id=None):
    all_feedback_items = Feedback.objects.all()
    active_feedback_items = all_feedback_items.exclude(status="C")

    #get blog from parameter passed in
    if id:
        single_feedback = all_feedback_items.get(id=id)
    else:
        single_feedback = None

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=single_feedback)
        if form.is_valid():
            form.save()
    else:
        if id:
            form = FeedbackForm(initial={
                    'user': single_feedback.user,
                    'status': single_feedback.status
                })
            form.fields['user'].widget.attrs['readonly'] = True
        else:
            form = FeedbackForm()

    return render(request, 'internalcontent/feedback.html',
        {'feedback':active_feedback_items, 'form':form})

def blogsites(request, id=None):
    all_blog_sites = BlogSite.objects.all()
    new_blog_sites = BlogSite.objects.filter(status="N")

    #get blog from parameter passed in
    if id:
        single_blog_site = all_blog_sites.get(id=id)
        if not single_blog_site.active:
            prev_inactive = True
        else:
            prev_inactive = False
    else:
        single_blog_site = None
        prev_inactive = False

    if request.method == 'POST':
        form = BlogSiteForm(request.POST, instance=single_blog_site)
        if form.is_valid():
            form.save()

            #if it was inactive and now active, send a welcome email
            if prev_inactive and single_blog_site.active:
                msg = EmailMessage('Travel Blog Source - Blog Site Approved',
                    get_template('emails/blogsiteactive.html').render(
                        Context({
                            'blogsite': single_blog_site,
                            'webURLroot' : settings.WEB_URL_ROOT
                        })
                    ),
                    settings.EMAIL_HOST_USER,
                    [single_blog_site.blog_owner.email, 'admin@travelblogsource.com']
                )
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()
    else:
        if id:
            form = BlogSiteForm(initial={
                'site_name': single_blog_site.site_name,
                'quick_info': single_blog_site.quick_info,
                'category': single_blog_site.category,
                'region': single_blog_site.region,
                'twitter': single_blog_site.twitter,
                'facebook': single_blog_site.facebook,
                'url': single_blog_site.url,
                'status': single_blog_site.status,
                'active': single_blog_site.active,
                'category': single_blog_site.category})
            form.fields['region'].widget.attrs['readonly'] = True
        else:
            form = BlogSiteForm()

    return render(request, 'internalcontent/blogsites.html',
        {'newblogsites':new_blog_sites, 'form':form})