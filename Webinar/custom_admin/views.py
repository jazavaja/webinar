from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from models.models import *


# Create your views here.
def delete_user(request, id):
    u = User.objects.get(id=id)
    u.delete()
    return redirect("admin_main")

def user(request):
    return render(request,"admin_users.html",{"users":User.objects.all()})
def edit_user(request, id):
    user = User.objects.get(id=id)
    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')
    email = request.POST.get('email')
    gender = request.POST.get('gender')
    birthday = request.POST.get('birthday')
    if username:
        user.username = username
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if email:
        user.email = email
    if gender:
        user.gender = gender
    if birthday:
        user.birthdate = birthday
    if password:
        pass
    user.save()
    return redirect("admin_main")
def create_user(request):
    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    gender = request.POST.get('gender')
    birthday = request.POST.get('birthday')
    check = User.objects.filter(email=email).first()
    if check:
        messages.error(request, "The email already exists.")
        return redirect("admin_main")
    check = User.objects.filter(username=username).first()
    if check:
        messages.error(request, "The username already exists.")
        return redirect("admin_main")
    if request.POST.get("is_staff") == "1":
        User.objects.create_user(username=username, password="123", first_name=first_name, last_name=last_name, email=email,birthdate=birthday,gender=gender,is_staff=True)
    else:
        User.objects.create_user(username=username, password="123", first_name=first_name, last_name=last_name, email=email,birthdate=birthday,gender=gender)
    return redirect("users")

def main_admin(request):
    return render(request, "admin_home.html", {"users": User.objects.all(), "webinars": Webinar.objects.all(),
                                          "subscriptions": Monthly_Subscription.objects.all(),
                                          "webinar_users": Webinar_User.objects.all(),
                                               "total_webinars":Webinar.objects.count(),
                                               "total_users":User.objects.count()})

def webinar(request):
    return render(request,"admin_webinars.html",{"webinars":Webinar.objects.all()})
def activate_webinar(request, id):
    webinar = Webinar.objects.get(id=id)
    webinar.type = "public"
    webinar.save()
    return redirect("admin_webinars")

def deactivate_webinar(request, id):
    webinar = Webinar.objects.get(id=id)
    webinar.type = "private"
    webinar.save()
    return redirect("admin_webinars")


def admin_sub(request):
    pass
