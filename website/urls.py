#  hello/urls.py

from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('home', views.home_page_view, name='home')
]
