from django.urls import path, include

from photos import views

urlpatterns = [
    path('', views.photo_display, name='photos'),
]
