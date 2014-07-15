from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.contrib.auth.models import User
from tbs.travel.models import Region, BlogSite, BlogEntry, Category
from tbs.reports.models import BlogSiteClick
import datetime
import calendar

def home(request):
    return render(request, 'reportscontent/home.html')

@login_required
def myblog(request, page, blog_id = None):
    currentUser = User.objects.get(username = request.user)
    currentUser_id = currentUser.id

    #get list of user's blogsites
    myblogsites = BlogSite.objects.filter(blog_owner=currentUser_id)

    #if user has multiple blog sites and a blogsite is not specified take the first one
    if myblogsites:
        if myblogsites.count > 1 and not blog_id:
            blogsite = myblogsites[0]
        elif myblogsites.count > 1 and blog_id:
            blogsite = myblogsites.filter(id = blog_id)
        else:
            blogsite = myblogsites
    else:
        blogsite = None

    #get previous months
    months = []
    normalarray = []
    postarray = []
    highlightarray = []
    toparray = []

    month_count = 3
    today = datetime.datetime.now()
    current_month = today.month

    #create the data for the graph, months, search total, post total
    for i in range(month_count):
        #get the previous MONTHS
        month = current_month - i
        if month < 1:
            month = 12 + month
        months.insert(0, calendar.month_name[month])

        #get the total blog site clicks in SEARCHES and POSTS
        normalTotal = BlogSiteClick.objects.filter(origin="SEARCH", sponsor_type = "NONE", blog_site = blogsite, click_date__month = month).count()
        postTotal = BlogSiteClick.objects.filter(origin="POST", blog_site = blogsite, click_date__month = month).count()
        highlightTotal = BlogSiteClick.objects.filter(origin="SEARCH", sponsor_type = "HIGH", blog_site = blogsite, click_date__month = month).count()
        topTotal = BlogSiteClick.objects.filter(origin="SEARCH", sponsor_type = "TOP", blog_site = blogsite, click_date__month = month).count()

        normalarray.insert(0, normalTotal)
        toparray.insert(0, topTotal)
        highlightarray.insert(0, highlightTotal)
        postarray.insert(0, postTotal)

    return render(request, 'reportscontent/myblog.html', {'page':page, 'blogsite':blogsite, 'myblogsites':myblogsites, 'months':months, 'normal':normalarray, 'top':toparray, 'highlight':highlightarray, 'blog':postarray})

def allblogs(request, page):
    #get previous months
    months = []
    searcharray = []
    postarray = []

    month_count = 3
    today = datetime.datetime.now()
    current_month = today.month

    #create the data for the graph, months, search total, post total
    for i in range(month_count):
        #get the previous MONTHS
        month = current_month - i
        if month < 1:
            month = 12 + month
        months.insert(0, calendar.month_name[month])

        #get the total blog site clicks in SEARCHES and POSTS
        searchTotal = BlogSiteClick.objects.filter(origin="SEARCH", click_date__month = month).count()
        postTotal = BlogSiteClick.objects.filter(origin="POST", click_date__month = month).count()

        searcharray.insert(0, searchTotal)
        postarray.insert(0, postTotal)

    return render(request, 'reportscontent/allblogs.html', {'page':page, 'months':months, 'searcharray':searcharray, 'postarray':postarray})

@staff_member_required
def admin(request, page):
    blogsiteclicks = BlogSiteClick.objects.all()
    blogsites = BlogSite.objects.filter(active=True)
    blogentries = BlogEntry.objects.all().order_by('-views')

    #aggregate value sets
    blogsiteclick_group_sums = blogsiteclicks.values('blog_site__site_name').annotate(count=Count('blog_site')).order_by('-count')
    blogsite_group_region = blogsites.values('region__display_value').annotate(count=Count('region')).order_by('-count')

    #set variables for the for loop below to assign data to months
    months = []
    normalarray = []
    postarray = []
    highlightarray = []
    toparray = []
    month_count = 3
    today = datetime.datetime.now()
    current_month = today.month

    #create the data for the graph, months, search total, post total
    for i in range(month_count):
        #get the previous MONTHS
        month = current_month - i
        if month < 1:
            month = 12 + month
        months.insert(0, calendar.month_name[month])

        #get the total blog site clicks in SEARCHES and POSTS
        normalTotal = blogsiteclicks.filter(origin="SEARCH", sponsor_type = "NONE", click_date__month = month).count()
        postTotal = blogsiteclicks.filter(origin="POST", click_date__month = month).count()
        highlightTotal = blogsiteclicks.filter(origin="SEARCH", sponsor_type = "HIGH", click_date__month = month).count()
        topTotal = blogsiteclicks.filter(origin="SEARCH", sponsor_type = "TOP", click_date__month = month).count()

        normalarray.insert(0, normalTotal)
        toparray.insert(0, topTotal)
        highlightarray.insert(0, highlightTotal)
        postarray.insert(0, postTotal)

    #Sponsorship report logic
    #get list of valid sponsors
    sponsor_blogs = blogsites.exclude(sponsor_type = "NONE")

    return render(request, 'reportscontent/admin.html', {'page':page, 'blogsiteclicks':blogsiteclicks, 'blogsites':blogsites,
        'blogsiteclick_group_sums': blogsiteclick_group_sums, 'blogentries':blogentries, 'blogsitecountries':blogsite_group_region,
        'months':months, 'normal':normalarray, 'top':toparray, 'highlight':highlightarray, 'blog':postarray, 'sponsor_blogs':sponsor_blogs})

#handles all the logic for the blogsearch tab on the reports app page
def blogsearch(request, page):
    countries = Region.objects.filter(region_type = "country", views__gt=0).order_by("-views", "display_value")
    continents = Region.objects.filter(region_type = "continent", views__gt=0).order_by("-views", "display_value")
    categories = Category.objects.order_by("-views", "display_value")

    return render(request, 'reportscontent/blogsearch.html',
        {'page':page, 'countries':countries, 'continents':continents,
        'categories':categories})