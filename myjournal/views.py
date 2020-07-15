from django.shortcuts import render
from myjournal.models import Journal
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class JournalListView(LoginRequiredMixin, ListView):
    model = Journal
    context_object_name = 'journals'
    #queryset = Platforms.objects.order_by().values('f_class','s_name').distinct()
    template_name = 'myjournal/journals.html'
  

