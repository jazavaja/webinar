from django.shortcuts import render
from models.models import *
# Create your views here.
def webinar_detail(request, id):
    webinar = Webinar.objects.get(id=id)
    print(webinar.name)
    return render(request, 'webinar-details.html',{'webinar':webinar})