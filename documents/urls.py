from django.urls import path
from documents import views

urlpatterns = [
    path('', views.document_display, name='documents')
]
