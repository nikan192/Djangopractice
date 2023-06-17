from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Games , Special_Games

# Create your views here.
class shop_view(ListView) :
    def get(self , request) :
        Gamseobj = Games.objects.all()
        Specgame = Special_Games.objects.all()

        Context1 : dict = {'Games' : Gamseobj}
        Context2 : dict = {'Spgames' : Specgame}

        combined_context = {**Context1 , **Context2}
        return render(request , 'index.html' , combined_context)
    
class pro_detail_game(DetailView) :
    model = Games
    template_name = 'mobilelist.html'
    context_object_name : str = 'game_d'
    pass


class spec_detail(DetailView) :
    model = Special_Games
    template_name = 'mobilelist.html'
    context_object_name : str = 'detail_special'
    pass




"""""""""
def game_d(request , detail_id) :

    detail = Games.objects.get(id = detail_id)
    detail_special = Special_Games.objects.get(id = detail_id)

    context1 = {'game_d' : detail}
    context2 = {'game_d2' : detail_special}

    combined_context = {**context1 , **context2}

    return render(request , 'mobilelist.html' , combined_context)
"""""""""""