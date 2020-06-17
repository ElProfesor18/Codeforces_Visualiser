from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import contactUs
from .models import enquiry

from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request,'login/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'login/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login/login.html', {})

def contact_us(request):
    
    if request.method == 'POST':
        form = contactUs(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            t = enquiry(name=name, email=email, subject=subject, message=message, copy=copy)
            t.save()

            mail_subject = 'Regarding the enquiry made on Codeforces Visualiser.'
            mail_message = ' It means a world to us. We will get back to you shortly.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail( subject, message, email_from, recipient_list )

            return index(request)

    else:
        form = contactUs()

    return render(request, 'login/contact_us.html', {'form' : form})

def email(request):
    subject = 'Regarding the enquiry made on Codeforces Visualiser.'
    message = ' It means a world to us. We will get back to you shortly.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('redirect to a new page')