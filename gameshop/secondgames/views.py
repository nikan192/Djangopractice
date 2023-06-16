from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Gametest

# Create your views here.


class test_view(ListView) :
    def get(self , request) :

        gameobj = Gametest.objects.all()

        Context = {'testgames' : gameobj}

        return render(request , 'index.html' , Context)
    
    pass