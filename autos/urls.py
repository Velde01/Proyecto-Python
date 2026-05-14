from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear_auto, name='crear_auto'),
    path('lista/', views.lista_autos, name='lista_autos'),
    path('buscar/', views.buscar, name='buscar_auto'),
    path('detalle/<int:id>/', views.detalle_auto, name='detalle_auto'),
    path('editar/<int:id>/', views.editar_auto, name='editar_auto'),
    path('borrar/<int:id>/', views.borrar_auto, name='borrar_auto'),
    path('about/', views.about, name='about'),
]