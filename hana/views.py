from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    response = redirect('home/')
    return response
    
def home(request):
    context={}
    return render(request, 'hana/index.html', context=context)