from django.urls import path
from documents import views
from documents import views
from documents.views import DocumentListView
urlpatterns = [
    path('', views.DocumentListView.as_view(), name='documents')
]
