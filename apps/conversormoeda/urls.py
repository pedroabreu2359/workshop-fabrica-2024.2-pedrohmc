from django.urls import path
from .views import conversao_moedas

urlpatterns = [
    path('', conversao_moedas, name='conversao_moedas')
]