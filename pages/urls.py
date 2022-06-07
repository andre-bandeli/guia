from django.contrib import admin
from django.urls import path
from .views import about, home, page_text, page_text_three, page_text_two

app_name = 'pages'

urlpatterns = [
    path('', home , name='home'),
    path('about/', about , name='about'),
    path('text/', page_text , name='page_text'),
    path('text-2/', page_text_two , name='page_text_two'),
    path('text-3/', page_text_three , name='page_text_three'),
]