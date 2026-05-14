from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path(
        'registro/',
        views.registro,
        name='registro'
    ),

    path(
        'login/',
        LoginView.as_view(
            template_name='accounts/login.html',
            next_page='/'
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(
            next_page='/'
        ),
        name='logout'
    ),

    path('perfil/', views.perfil, name='perfil'),

    path(
    'editar-perfil/',
        views.editar_perfil,
        name='editar_perfil'
    ),
]