from django.shortcuts import render
from .api import check_air

def index(request):
    res = check_air()
    loc = request.POST['location']
    pm10 = res.get(loc)
    context = {'station' : '고현동', 'pm10' : pm10}
    return render(request, 'dust_checker/dust_main.html', context)

def detail(request):
    res=check_air()
    context = {'dust' : res}
    return render(request, 'dust_checker/dust_detail.html', context)

# Create your views here.
