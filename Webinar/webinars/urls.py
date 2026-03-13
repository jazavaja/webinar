from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>/', views.webinar_detail, name='webinar_detail'),
    path('add/', views.add_webinar, name='add_webinar'),
]