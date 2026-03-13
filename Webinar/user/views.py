from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect

from models.models import *


# Create your views here.

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password != password_confirm:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email,age=age,gender=gender)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['user'] = user.id
            # Session.objects.create(logged=user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')
def logout(request):
    del request.session['user']
    return redirect('home')
def Account(request):
    if request.method == 'POST':
        log = request.POST.get('logout')
        if log == 'yep':
            del request.session['user']
            return redirect('home')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        user = User.objects.get(id=request.session.get('user'))
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        if password:
            user.set_password(password)
        user.save()
        return redirect('account')
    if request.session.get('user') is None:
        return redirect('login')
    user = User.objects.get(id=request.session.get('user'))

    your_webinars = []
    others_webinars = []
    for webinar in Webinar_User.objects.filter(user_id=user.id).all():

        i = Webinar.objects.get(id=webinar.webinar_id_id)
        if not i:
            pass

        if webinar.role == Role_webinar.HOST.value:
            your_webinars.append(i)
        else:
            others_webinars.append(i)
    return render(request, 'account.html',{'user':user,'your_webinars':your_webinars,'other_webinars':others_webinars})