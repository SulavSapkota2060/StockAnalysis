from django.urls import path
from . import views


urlpatterns = [
   path('',views.tasks,name='tasks'),
   path('chart/',views.chart,name='charts')
]