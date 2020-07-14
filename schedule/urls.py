from django.urls import path
from schedule import views
from schedule.views import ScheduleListView
urlpatterns = [
    path('', ScheduleListView.as_view(), name='schedule')
]
