from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListUsuario.as_view()),
    path('<int:pk>/', views.DetailUsuario.as_view()),
]