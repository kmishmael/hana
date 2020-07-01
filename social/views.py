from django.shortcuts import render
from django.views import generic
from social.models import Platforms
from django.shortcuts import get_object_or_404

# Create your views here.

class PlatformsListView(generic.ListView):
    model = Platforms
    context_object_name = 'socials'   
    queryset = Platforms.objects.all()
    template_name = 'social.html'
     
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PlatformsListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        return context

class PlatformsDetailView(generic.DetailView):
    model = Platforms
    def book_detail_view(self, request, primary_key):
        platforms = get_object_or_404(Platforms, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'platfroms': platforms})