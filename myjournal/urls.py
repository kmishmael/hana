from django.urls import path
from myjournal import views
urlpatterns = [
    path('',views.journal_display, name='display_journal'),
]
