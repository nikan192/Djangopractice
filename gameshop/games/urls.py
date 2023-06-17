from django.urls import path
from . import views

urlpatterns = [
    path('newgames/' , views.shop_view.as_view() , name='Gameshop'),
    path('newgames/<str:pk>/' , views.pro_detail_game.as_view() , name='Gamepage')
]
