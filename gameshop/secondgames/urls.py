from django.urls import path
from .views import test_view

urlpatterns = [
    path('testgames/' , test_view.as_view() , name='Testmod')
]
