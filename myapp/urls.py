from django.urls import path
from . import views

urlpatterns = [
    path('<str:url>/', views.menu_page, name='menu_page'),
    path('', views.index, name='index'),
]
