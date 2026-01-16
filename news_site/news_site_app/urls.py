from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    
    #Страница авторизации
    path('auth/', views.auth, name='auth'), # name - это имя маршрута

    #Страница регистрации
    path('reg/', views.reg, name='reg'),

    path('logout/', views.logout_view, name='logout')
]

