from django.shortcuts import render
from documents.models import Document
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class DocumentListView(LoginRequiredMixin, ListView):
    model = Document
    context_object_name = 'documents'
    #queryset = Platforms.objects.order_by().values('f_class','s_name').distinct()
    template_name = 'documents/documents.html'
  
