from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_create, name='film_create'),
    path('list/', views.film_list, name='film_list'),
]
