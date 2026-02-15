from django.shortcuts import render
from models.models import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def webinar(request):
    w = Webinar.objects.all()
    return render(request, 'webinar.html', {'webinars':w})