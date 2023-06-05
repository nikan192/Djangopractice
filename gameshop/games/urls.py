from django.urls import path , include
from django.conf.urls.static import static
from django.conf import Settings
from .views import shop_view

urlpatterns = [
    path('newgames/' , shop_view.as_view() , name='Gameshop')    
]
