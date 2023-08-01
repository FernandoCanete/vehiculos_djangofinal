from django.urls import path, include
from . import views

urlpatterns = [
    path('add', views.add, name="add"),
    path('list', views.list, name="list"),
]