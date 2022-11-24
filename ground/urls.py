from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('home/', views.home, name='ground'),
    path('add-city/', views.addCity, name='addCity'),
    path('create-city/', views.createCity, name='createCity'),
    path('add-ground/', views.addGround, name='addGround'),
    path('create-ground/', views.createGround, name='createGround')
]