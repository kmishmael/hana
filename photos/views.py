from django.shortcuts import render
from django.template import loader
import pandas as pd
import csv 
from django.views.generic import ListView, DetailView
from photos.models import Image

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class ImageListView(LoginRequiredMixin, ListView):
    model = Image
    context_object_name = 'images'
    #queryset = Platforms.objects.order_by().values('f_class','s_name').distinct()
    template_name = 'photos/photos.html'
  

'''
# Create your views here.
def photo_display(request):
    file = open("photos/static/photos/csv/driveimages.csv", "r", newline='')
    #df = pd.read_csv(file)
    #images = df['url']
    reader = csv.DictReader(file)
    dict_list = []
    for line in reader:
        dict_list.append(line)
    images = dict_list
    #template = loader.get_template('photos/photos.html')
    return render(request, 'photos/photos.html', {'images': images})
'''
