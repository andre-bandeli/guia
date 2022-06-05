from django.contrib import admin
from django.urls import path
from .views import index, about, home

urlpatterns = [
    path('', index , name='index'),
    path('home/', home , name='home'),
    path('about/', about , name='about'),
]