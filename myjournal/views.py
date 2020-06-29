from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from datetime import datetime



# Create your views here.
def index(request):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%I:%M %Z")
    context = {
        'date': date,
        'time': time,
    }
    return render(request, 'hana/index.html', context=context)

