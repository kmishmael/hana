from django.shortcuts import render

from django.views.generic import ListView, DetailView
from videos.models import Video

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class VideoListView(LoginRequiredMixin, ListView):
    model = Video
    context_object_name = 'videos'
    #queryset = Platforms.objects.order_by().values('f_class','s_name').distinct()
    template_name = 'videos/videos.html'
  