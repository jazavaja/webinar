from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.Account, name='account'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('delete/', views.Login, name='delete'),
    path('logout/', views.Logout, name='logout'),
]