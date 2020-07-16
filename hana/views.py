from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views import View

def index(request):
    response = redirect('home/')
    return response

@login_required
def home(request):
    context={}
    return render(request, 'hana/index.html', context=context)

def login(request):
    context = {}
    return render(request, 'social/login.html', context=context)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'social/register.html'
    class Meta:
        help_texts = {
            'username': None,
            'password1': None,
        }
