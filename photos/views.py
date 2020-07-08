from django.shortcuts import render

# Create your views here.
def photo_display(request):
    context={}
    return render(request, 'hana/main-display.html', context=context)