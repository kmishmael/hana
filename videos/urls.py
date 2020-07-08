from django.urls import path
from videos import views

urlpatterns = [
    path('', views.display_videos, name='video_display'),
]
