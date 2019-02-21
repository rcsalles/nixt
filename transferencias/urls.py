from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTransferencia.as_view()),
    path('<int:pk>/', views.DetailTransferencia.as_view()),
]