from django.contrib import admin
from django.urls import path
from social import views
from django.views.generic import ListView, DetailView
from social.views import SignUp
urlpatterns = [
   path('register/', views.SignUp.as_view(), name='register'),
   # path('social/<int:pk>/', views.PlatformsDetailView.as_view(), name='platform_detail'),
   # path('home/', views.PlatformsListView.as_view(), name='home'),
]
              