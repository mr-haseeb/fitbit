from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response




class MainPageView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'dashborad/main.html')


class ChartsPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashborad/charts2.html')

class ChartsData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "data": [12, 19, 3, 5, 2, 3, 10],
        }   

        return Response(data)

