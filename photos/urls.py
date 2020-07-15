from django.urls import path, include

from photos import views
from photos.views import ImageListView
urlpatterns = [
    path('', views.ImageListView.as_view(), name='photos'),
]
