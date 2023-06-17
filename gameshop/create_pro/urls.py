from django.urls import path
from .views import GameCreate , GameEdit , GameDelete , GameSpecialCreate  


urlpatterns = [
    path('create/' , GameCreate.as_view() , name='Gamecreate'),
    path('edit/<int:pk>/' , GameEdit.as_view() , name='Gameedit'),
    path('delete/<int:pk>/' , GameDelete.as_view() , name='Gamedelete')
]
