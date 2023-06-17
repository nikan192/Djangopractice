from django.shortcuts import render
from django.views.generic.edit import CreateView , UpdateView

from games.models import Games , Special_Games

# Create your views here.

class GameCreate(CreateView) :
    model = Games
    template_name = 'new-pro.html'
    fields = ['image' , 'name' , 'description' , 'price']
    pass

class GameSpecialCreate(CreateView) :
    model = Special_Games
    template_name = 'new-pro-spec.html'
    fields = ['image' , 'name' , 'description' , 'price']
    pass


class GameSpecialCreate(UpdateView) :
    model = Special_Games
    template_name = 'new-pro-spec.html'
    fields = ['image' , 'name' , 'description' , 'price']
    pass



class GameEdit(UpdateView) :
    model = Games
    template_name = 'edit-pro.html'
    fields = ['image' , 'name' , 'description' , 'price']
    pass