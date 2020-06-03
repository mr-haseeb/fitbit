from django.urls import path
from .views import MainPageView,ChartsData,ChartsPageView


urlpatterns = [

    path('',MainPageView.as_view(),name='dashborad-main'),
    path('charts/',ChartsPageView.as_view(),name='dashborad-charts'),
    path('api/charts/data/', ChartsData.as_view(),name='dashborad-charts-api')

]