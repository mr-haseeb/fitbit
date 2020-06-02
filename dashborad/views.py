from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import messages

from .models import Health
from django.core import serializers


# Create your views here.
def home(request):
    return render(request, 'dashborad/base.html')





