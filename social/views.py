from django.shortcuts import render
from django.views import generic
from social.models import Platforms
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class PlatformsListView(LoginRequiredMixin, ListView):
    model = Platforms
    context_object_name = 'platforms'
    #queryset = Platforms.objects.order_by().values('f_class','s_name').distinct()
    template_name = 'hana/index.html'
    
    
class PlatformsDetailView(LoginRequiredMixin, DetailView):
    model = Platforms
    template_name = 'social/platform-detail.html'

class SocialListView(LoginRequiredMixin, ListView):
    model = Platforms
    context_object_name = 'platforms'
    template_name = 'social/main-social.html'
'''
class PlatformsListView(generic.ListView):
    model = Platforms
    context_object_name = 'socials'   
    template_name = 'social.html'
    
    def get_queryset(self):
        return Platforms.objects.all()
     
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PlatformsListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        return context

class PlatformsDetailView(generic.DetailView):
    model = Platforms
    def platforms_detail_view(request, primary_key):
    try:
        platforms = Platforms.objects.get(pk=primary_key)
    except Platforms.DoesNotExist:
        raise Http404('Platform does not exist')
    
    return render(request, 'social/social.html', context={'Platforms': Platforms})'''