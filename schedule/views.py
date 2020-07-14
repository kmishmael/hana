from django.shortcuts import render

from django.views.generic.list import ListView
import csv

# Create your views here
class ScheduleListView(ListView):
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