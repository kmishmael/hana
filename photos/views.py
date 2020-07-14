from django.shortcuts import render
from django.template import loader
import pandas as pd
import csv 

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