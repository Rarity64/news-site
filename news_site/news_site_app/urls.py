from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    
    #Страница авторизации
    path('auth/', views.auth, name='auth'), # name - это имя маршрута

    #Страница регистрации
    path('reg/', views.reg, name='reg'),

    path('logout/', views.logout_view, name='logout'),

    path('news/<int:id>', views.news_template, name='news'),

    path('item/<int:id>', views.item_template, name='item'),

    path('news/', views.news_list, name='news_list')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

