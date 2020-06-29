from django.shortcuts import render

from social.models import Name
# Create your views here.
def index(request):
    context = {
        'platform': Name.type,
        'email': Name.email,
        'name': Name.name,
        'username': Name.username,
        'password': Name.password,
    }
    return render(request, 'social/social.html', context=context)

