"""
URL configuration for blogProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('home/', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('update-room/<str:pk>/', views.updateRoom, name='updateRoom'),
    path('userprofile/<str:pk>/', views.userProfile, name='userprofile'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='deleteRoom'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('create-room/', views.createRoom, name='createRoom'),
]
