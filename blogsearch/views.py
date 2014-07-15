from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tbs.travel.models import Region, BlogSite, BlogSiteReview, BlogEntry, BannerPic, Category
from tbs.reports.models import BlogSiteClick, BannerPicClick
import json
import datetime

m_today = datetime.date.today()

#home page for choosing search criteria
def home(request):
    #get count of active blogsites per country since can't filter on method
    blog_sites = BlogSite.objects.filter(active=True)
    id_list = []
    for blog_site in blog_sites:
        if blog_site.region:
            id_list.append(blog_site.region.id)

    countries = Region.objects.filter(id__in=id_list)
    continents = Region.objects.filter(region_type = 'Continent')
    categories = Category.objects.all()

    return render(request, 'blogsearchcontent/home.html', {
        'countries':countries, 'continents':continents, 'categories':categories})

#returns the page for the search. As of now it's either a country or a continent
def search(request, type, searchValue):
    #logic specific to regional searches
    if type == "region":
        show_blog_entries = True
        search = Region.objects.get(value=searchValue, active=True)
        blog_sites = BlogSite.objects.filter(region=search.id, active=True)
        blog_entries = BlogEntry.objects.filter(region=search.id, active=True, active_date__lte=m_today).order_by("-id")

        #if banner_pic doesn't exist, need to return null. If multiple, take first.
        try:
            banner_pic = BannerPic.objects.get(region=search.id, active=True, active_date__lte=m_today)
        except BannerPic.MultipleObjectsReturned:
            banner_pic = BannerPic.objects.filter(region=search.id, active=True)[0]
        except BannerPic.DoesNotExist:
            banner_pic = None

        #add a view to the region
        if search.views:
            search.views += 1
        else:
            search.views = 1
        search.save()

        #pass display value to template
        search = search.display_value

    #logic specific to text searches
    elif type == "text":
        show_blog_entries = False
        search = searchValue
        blog_sites = BlogSite.objects.filter(quick_info__icontains=searchValue)
        blog_entries = None
        banner_pic = None

    #logic specific to category
    elif type == "category":
        show_blog_entries = True
        search = Category.objects.get(value=searchValue, active=True)
        blog_sites = BlogSite.objects.filter(category=search.id, active=True)
        blog_entries = BlogEntry.objects.filter(blog_site__category=search.id, active=True, active_date__lte=m_today).order_by("-id")

        #if banner_pic doesn't exist, need to return null. If multiple, take first.
        try:
            banner_pic = BannerPic.objects.get(category=search.id, active=True, active_date__lte=m_today)
        except BannerPic.MultipleObjectsReturned:
            banner_pic = BannerPic.objects.filter(category=search.id, active=True)[0]
        except BannerPic.DoesNotExist:
            banner_pic = None

        #add a view to the region
        if search.views:
            search.views += 1
        else:
            search.views = 1
        search.save()

        #pass display value to template
        search = search.display_value

    #shared logic between all search types
    if blog_entries:
        blog_entries_1 = blog_entries[0]
        blog_entries_2 = blog_entries[1:3]
        blog_entries_3 = blog_entries[3:6]
    else:
        blog_entries_1 = None
        blog_entries_2 = None
        blog_entries_3 = None

    #can only get rated if the user is logged in
    #must return something and not AnonymousUser
    if request.user.is_authenticated():
        rated = BlogSiteReview.objects.filter(user=request.user).values_list(
            'blog_site', flat=True)
    else:
        rated = False

    return render(request, 'blogsearchcontent/search.html', {'search':search,
        'blogentries1':blog_entries_1, 'blogentries2':blog_entries_2,
        'blogentries3':blog_entries_3, 'blogsites':blog_sites, 'rated':rated,
        'bannerpic':banner_pic, 'showblogentries':show_blog_entries})

@login_required
def setrating(request):
    if request.is_ajax():
        if request.method == 'POST':
            rating = json.loads(request.POST['rate'])
            blog_site = BlogSite.objects.get(id=json.loads(request.POST['idBox']))
            sponsor = "None" #todo: need to pass this in

            #save rating
            review = BlogSiteReview()
            review.user = request.user
            review.blog_site = blog_site
            review.review_rating = rating
            review.sponsor_level = sponsor
            review.save()

    return HttpResponse("save successful")

def blogsiteclick(request):
    if request.is_ajax():
        if request.method == 'POST':
            #will need to add a blogsiteclick from JSON
            blog_site = BlogSite.objects.get(id=request.POST['blog_id'])
            origin = request.POST['origin']
            sponsor = request.POST['sponsor']

            click = BlogSiteClick()
            click.blog_site = blog_site
            click.click_date = m_today
            click.origin = origin
            click.sponsor_type = sponsor
            click.save()

    return HttpResponse("success for " + request.POST['blog_id'] + " from " + origin + " on " + str(m_today))

def bannerpicclick(request):
    if request.is_ajax():
        if request.method == 'POST':
            #will need to add a blogsiteclick from JSON
            banner_pic_id = BannerPic.objects.get(id=request.POST['banner_pic_id'])

            click = BannerPicClick()
            click.banner_pic = banner_pic_id
            click.click_date = m_today
            click.save()

    return HttpResponse("success for " + request.POST['banner_pic_id'] + " on " + str(m_today))

def blog(request, blog_id):
    blog = BlogEntry.objects.get(id=blog_id)

    #add a view to the entry
    if blog.views:
        blog.views += 1
    else:
        blog.views = 1
    blog.save()

    return render(request, 'blogsearchcontent/blog.html', {'blog':blog})