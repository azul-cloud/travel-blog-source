from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from tbs.travel.models import HelpTopic, Error
from tbs.travel.forms import ContactForm, UserForm, UserUpdateForm, FeedbackForm

def home(request):
    return render(request, 'content/home.html')

# moved to their own apps
# def blogowner(request):
#     return render(request, 'content/blogowner/home.html')

# def search(request):
#     return render(request, 'content/search/home.html')

def about(request):
    return render(request, 'content/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['body'],
                'admin@travelblogsource.com',
                [cd.get('email', 'admin@travelblogsource.com')])
            return render(request, 'content/generictext.html',
                {'text':'Your contact has been successfully sent, thank you.'})
    else:
        form = ContactForm()
    return render(request, 'content/contact.html', {'form': form})

def help(request, group = None):
    if group:
        helptopics = HelpTopic.objects.filter(group=group, active=True)
    else:
        helptopics = HelpTopic.objects.filter(active=True)
    return render(request, 'content/help.html', {'helptopics':helptopics})

def blog(request):
    return blog(request, 'content/blog.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)

            #send welcome email
            msg = EmailMessage('Travel Blog Source - Activate User Registration',
                get_template('emails/userregister.html').render(
                    Context({
                        'user': new_user,
                        'webURLroot' : settings.WEB_URL_ROOT
                    })
                ),
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']]
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()

            return render(request, "content/generictext.html",
                {'text': 'Thank you for registering. You should receive an email shortly with a link to verify your email with your account.'})
        else:
            return render(request, "registration/register.html", {'form': form})
    else:
        form = UserForm()
        return render(request, "registration/register.html", {'form': form})

#for users to submit feedback such as errors, comments, or suggestions
@login_required
def feedback(request):
    user = User.objects.get(username = request.user)
    #currentUser_id = currentUser.id

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = user
            feedback.status = 'S'

            feedback.save()
            return render(request, 'content/generictext.html',
                {'text':'Your feedback has been received, thank you. It is feedback like this that improves Travel Blog Source.'})
        else:
            #form not valid
            error = Error.objects.get(id=2)
            return render(request, 'content/error.html', {'error':error,})
    else:
        form = FeedbackForm(initial={'user':user.id})
        return render(request, 'content/feedback.html', {'form': form})

@login_required
def updateprofile(request):
    instance = User.objects.get(username = request.user)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return render(request, 'content/generictext.html', {'text':'Your profile was successfully updated.'})
        return render(request, 'registration/update.html', {'form':form})
    else:
        form = UserUpdateForm()
        #form.fields['password1'].widget = forms.HiddenInput()
        #form.fields['password2'].widget = forms.HiddenInput()

        #set initial values
        form.initial['username'] =instance.username
        form.initial['first_name'] = instance.first_name
        form.initial['email'] = instance.email

        form.fields['username'].widget.attrs['readonly'] = True

        return render(request, 'registration/update.html', {'form':form, 'user':instance})

def testing(request):
    return render(request, 'content/testing.html',
        {})

def verifyemail(request, salthash):
    return render(request, 'content/generictext.html',
        {'text':'Thank you, your email has now been verified and your account is fully registered.'})