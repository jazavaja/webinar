from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.Account, name='account'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]