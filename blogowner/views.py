from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from tbs.travel.models import BlogSite, Error
from tbs.blogowner.forms import BlogSiteForm, BlogEntryForm, BannerPicForm
from django import forms

def home(request):
    return render(request, 'blogownercontent/home.html')

#Displays sponsorship opportunities
def sponsor(request):
    return render(request, 'blogownercontent/sponsor.html')

#Registers a Blog Site for the logged in user
@login_required
def register(request):
    if request.method == 'POST':
        form = BlogSiteForm(request.POST)
        if form.is_valid():
            blogSite = form.save(commit=False)
            currentUser = User.objects.get(username = request.user)
            currentUser_id = currentUser.id
            blogSite.blog_owner_id = currentUser_id
            blogSite.save()
            return render(request, 'content/generictext.html',
                {'text': 'Thank you for registering your travel blog. We will be reviewing it shortly and you should see it on the blog search page.'})
        else:
            return render(request, 'blogownercontent/register.html', {'form':form})

    else:
        form = BlogSiteForm()
        return render(request, 'blogownercontent/register.html', {'form':form})


#page to display general info to blog owners
def info(request):
    return render(request, 'blogownercontent/info.html')

#This will update a Blog Site profile of the logged in user
@login_required
def updatesites(request, blog_id=None):
    currentUser = User.objects.get(username = request.user)
    currentUser_id = currentUser.id

    #get blogsite that will be updated, and the list of possible blogsites
    try:
        blogsites = BlogSite.objects.filter(blog_owner=currentUser_id)
        if not blog_id:
            form_blogsite = blogsites[0]
        else:
            form_blogsite = blogsites.get(id=blog_id)
    except IndexError:
        #User does not have any blog sites
        error = Error.objects.get(id=1)
        return render(request, 'content/error.html', {'error': error})

    #if post, either delete or update, else display the Blog Site form
    if request.method == 'POST':
        instance = BlogSite.objects.get(id=form_blogsite.id)

        #either update the blogsite, or delete it
        if 'update' in request.POST:
            form = BlogSiteForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return render(request, 'blogownercontent/updatesites.html',
                    {'blogsites':blogsites, 'form': form, 'sent':True})
        ####Delete has been disabled and replaced by the active field####
        #elif 'delete' in request.POST:
        #    #instance.delete()
        #    return render(request, 'blogownercontent/blogsitedeleted.html', {'sitename':instance.site_name})
        else:
            #the post data was not recognized
            error = Error.objects.get(id=3)
            return render(request, 'content/error.html', {'error': error})
    else:
        form = BlogSiteForm(initial={'site_name':form_blogsite.site_name,
            'url':form_blogsite.url, 'region':form_blogsite.region,
            'category':form_blogsite.category,
            'twitter':form_blogsite.twitter, 'facebook':form_blogsite.facebook,
            'quick_info':form_blogsite.quick_info, 'active':form_blogsite.active})
        form.fields['site_name'].widget.attrs['readonly'] = True

    return render(request, 'blogownercontent/updatesites.html', {'blogsites':blogsites, 'form': form})

#used for uploads from blogowners.
#Right now it's just blog entries and banner pics
@login_required
def upload(request, type =  None):
    if type == "blog":
        blogsites = BlogSite.objects.filter(blog_owner=request.user)
        if request.method == 'POST':
            form = BlogEntryForm(request.POST, request.FILES)

            #if form is not valid, need to apply these filters again
            form.fields['active'].widget = forms.HiddenInput()
            form.fields['user'].widget = forms.HiddenInput()
            form.fields['blog_site'].queryset = blogsites

            if form.is_valid():
                form.save()
                return render(request, 'content/generictext.html', {'text':'Your Blog Entry has been submitted. It will be reviewed and we will send you an update. If you have questions, please read the FAQ or Contact Us.'})
            else:
                return render(request, 'blogownercontent/upload.html', {'type':type, 'form':form})
        else:
            form = BlogEntryForm(initial={'user': request.user})
            form.fields['active'].widget = forms.HiddenInput()
            form.fields['user'].widget = forms.HiddenInput()
            form.fields['blog_site'].queryset = blogsites
            return render(request, 'blogownercontent/upload.html', {'type':type, 'form':form})
    elif type == "bannerpic":
        default_form = BannerPicForm(initial={'user': request.user})
        default_form.fields['user'].widget = forms.HiddenInput()
        default_form.fields['active_date'].widget = forms.HiddenInput()
        default_form.fields['active'].widget = forms.HiddenInput()
        default_form.fields['status'].widget = forms.HiddenInput()

        if request.method == 'POST':
            form = BannerPicForm(request.POST, request.FILES)
            form.fields['user'].widget = forms.HiddenInput()
            form.fields['active'].widget = forms.HiddenInput()
            form.fields['status'].widget = forms.HiddenInput()
            form.fields['active_date'].widget = forms.HiddenInput()

            if form.is_valid():
                form.save()
                return render(request, 'blogownercontent/upload.html',
                    {'sent': True, 'type':type, 'form':default_form })

            #if not valid
            return render(request, 'blogownercontent/upload.html',
                {'type':type, 'form':form})
        else:
            return render(request, 'blogownercontent/upload.html',
                {'type':type, 'form':default_form})
    else:
        return render(request, 'blogownercontent/upload.html', {'type':type})