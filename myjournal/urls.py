from django.urls import path
from myjournal import views
from myjournal.views import JournalListView
urlpatterns = [
    path('',views.JournalListView.as_view(), name='journals'),
]
