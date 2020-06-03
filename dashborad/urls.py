from django.urls import path
from .views import HomePageView, ChartData,ChartPageView,MainPageView


urlpatterns = [

    path('', HomePageView.as_view(),name='dashborad-home'),
    path('chart/',ChartPageView.as_view(),name='dashborad-chart'),
    path('main/',MainPageView.as_view(),name='dashborad-main'),
    path('api/chart/data/', ChartData.as_view(),name='dashborad-chart-api')
]