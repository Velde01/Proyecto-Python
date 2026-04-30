from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('crear/', views.crear_auto),
    path('lista/', views.lista_autos),
    path('buscar/', views.buscar),
]