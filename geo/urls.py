from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pounds/', views.pounds, name='pounds'),
    path('pound/', views.pounds, name='pounds'),
    path('pound/new/', views.pound_new, name='pound_new'),
]