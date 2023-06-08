from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Games , Special_Games

# Create your views here.
class shop_view(ListView) :
    def get(self , request) :
        Gamseobj = Games.objects.all()
        Specgame = Special_Games.objects.all()

        Context1 = {'Games' : Gamseobj}
        Context2 = {'Spgames' : Specgame}

        combined_context = {**Context1 , **Context2}
        return render(request , 'index.html' , combined_context)
    pass