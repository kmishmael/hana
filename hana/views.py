from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    response = redirect('login/')
    return response

@login_required
def home(request):
    context={}
    return render(request, 'hana/index.html', context=context)

def login(request):
    context = {}
    return render(request, 'social/login.html', context=context)