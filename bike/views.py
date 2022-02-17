from django.shortcuts import render
from .api import bike

def index(request):
    res=bike()
    context = {'aa'}
    
    return render(request, 'bike/bike_main.html', context)

def detail(request):
    res=bike()
    context={'bike':res}
    return render(request, 'bike/bike_detail.html', context)
