from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newClient/', views.createNewClient, name='newClient'),
    path('<int:client_id>/', views.clientDetail, name='clientDetail'),
    path('<int:client_id>/newInvoice/', views.newInvoice, name='newInvoice'),
]
