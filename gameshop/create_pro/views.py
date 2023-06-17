from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from games.models import Games , Special_Games

# Create your views here.

class GameCreate(CreateView) :
    model = Games
    template_name = 'new-pro.html'
    fields = ['image' , 'name' , 'description' , 'price']
    pass

class GameEdit(UpdateView) :
    model = Games
    template_name = 'edit-pro.html'
    fields = ['image' , 'name' , 'description' , 'price']
    pass

class GameDelete(DeleteView) :
    model = Games
    template_name = 'delete-pro.html'
    success_url = reverse_lazy('Gameshop')
    pass

class GameSpecialCreate(CreateView) :
    model = Special_Games
    template_name = 'new-pro-spec.html'
    fields = ['image' , 'name' , 'description' , 'price']
    pass


class GameSpecialEdit(UpdateView) :
    model = Special_Games
    template_name = 'new-pro-spec.html'
    fields = ['image' , 'name' , 'description' , 'price']
    pass