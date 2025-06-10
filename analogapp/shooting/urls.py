from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('film/new/', views.film_create, name='film_create'),
    path('kosul/new/', views.kosul_create, name='kosul_create'),
    path('poz/new/', views.poz_create, name='poz_create'),
]
