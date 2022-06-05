from django.contrib import admin
from django.urls import path
from .views import index, about, home, page_text

app_name = 'pages'

urlpatterns = [
    path('', index , name='index'),
    path('home/', home , name='home'),
    path('about/', about , name='about'),
    path('text/', page_text , name='page_text'),
]