from django.urls import path
from .views import shop_view

urlpatterns = [
    path('newgames/' , shop_view.as_view() , name='Gameshop')    
]
