from django.urls import path
from videos import views
from videos.views import VideoListView
urlpatterns = [
    path('', views.VideoListView.as_view(), name='videos'),
]
