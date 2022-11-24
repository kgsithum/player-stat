from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='player'),
    path('add-player/', views.addPlayer, name='addPlayer'),
    path('create/', views.create, name='create'),
    path('get-player/', views.getPlayer, name='getPlayer')
]