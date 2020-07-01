from django.contrib import admin
from django.urls import path
from social import views

urlpatterns = [
    path('social/', views.PlatformsListView.as_view(), name='social'),
    path('social/<int:pk>', views.PlatformsDetailView.as_view(), name='social-detail'),
]
