from django.urls import path

from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('webinar/', views.webinar, name='webinar'),
    path('contact/', views.contact, name='contact_us'),
    path('about_us/', views.about_us, name='about_us'),
]