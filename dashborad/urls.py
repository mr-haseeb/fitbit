from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashborad-home'),
    path('charts/',views.charts,name='dashborad-charts')

]