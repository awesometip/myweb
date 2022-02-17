from django.urls import path
from . import views

app_name = 'bike'

urlpatterns = [
    path('', views.index, name='index'),
    
]