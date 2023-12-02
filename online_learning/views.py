from django.shortcuts import render
from django.http import HttpResponse
from .models import Persons

# Create your views here.

def user(request):
    return render(request, 'static/home.html')