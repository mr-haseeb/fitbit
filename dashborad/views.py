from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response




class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashborad/base.html')

class ChartPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashborad/chart.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "data": [12, 19, 3, 5, 2, 3, 10],
        }   

        return Response(data)