from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from models.models import *
# Create your views here.
def home(request):
    webinars = Webinar.objects.all()
    special_webinars = []
    for i in webinars:
        type = Category_Webinar.objects.filter(webinar_id=i.id).first()
        cat = Type.objects.filter(id=type.category_id).first()
        if cat.name == 'Special':
            print(i.name)
            special_webinars.append(i)
    return render(request, 'home.html', {'webinars':webinars, 'special_webinars':special_webinars})
def contact(request):
    return render(request, 'contact-us.html')
def about_us(request):
    return render(request, 'about-us.html')

def webinar(request):
    w = Webinar.objects.all()
    spe = []
    sp = Webinar.objects.all()
    for i in sp:
        if i.type == 'public':
            type = Category_Webinar.objects.filter(webinar_id=i.id).first()

            cat = Type.objects.filter(id=type.category_id).first()

            if cat.name == 'Special':
                spe.append(i)
    sli = []
    sl = Webinar.objects.all()
    for i in sl:
        if i.type == 'public':
            type = Category_Webinar.objects.filter(webinar_id=i.id).first()
            cat = Type.objects.filter(id=type.category_id).first()
            if cat.name == 'Sliding':
                sli.append(i)
    for i in sp:
        if i.type == 'public':
            type = Category_Webinar.objects.filter(webinar_id=i.id).first()
            cat = Type.objects.filter(id=type.category_id).first()
            if cat.name == 'Special':
                sli.append(i)

    return render(request, 'webinar.html', {'webinars':w, 'special_webinars':spe, 'slider_webinars':sli})