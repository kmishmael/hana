from django.shortcuts import render

from django.views.generic.list import ListView
import csv
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here
class ScheduleListView(LoginRequiredMixin, ListView):
    template_name = 'schedule/schedule.html'
    def get_queryset(self):
        file = open("photos/static/photos/csv/driveimages.csv", "r", newline='')
        reader = csv.DictReader(file)
        dict_list = []
        for line in reader:
            dict_list.append(line)
        images = dict_list 
        return images
    #return render(request, 'photos/photos.html', {'images': images})