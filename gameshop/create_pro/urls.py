from django.urls import path
from .views import GameCreate , GameEdit , GameSpecialCreate  


urlpatterns = [
    path('create/' , GameCreate.as_view() , name='Gamecreate'),
    path('edit/<str:pk>/' , GameEdit.as_view() , name='Gameedit')
]
