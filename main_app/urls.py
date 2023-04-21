from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('about/', views.about),
    path('services/', views.services),
    path('portfolio/', views.portfolio),
    path('contact/', views.contact),
]