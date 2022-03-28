from django.urls import path ,include
from .views import  IndexView

urlpatterns = [

    # path('endereço/', IndexView.as_view(), name='nome-da-url'),
    path('inicio/', IndexView.as_view(), name='inicio'),

]