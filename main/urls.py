from django.urls import path
from main.views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('putovanja/', PutovanjeList.as_view(), name='putovanja'),
    path('prijave/', PrijaveList.as_view()),
    path('putovanja_hr/', PutovanjaCroatiaList.as_view(), name='putovanja_hr'),
    path('putovanje/<int:putovanje_sifraPutovanja>/', views.PutovanjeDetailView.as_view(), name='putovanje_detail'),
    path('putovanja/dodaj', views.add_putovanje, name='add_putovanja'),
    path('putovanja/uredi/<int:pk>', views.update_putovanje, name='update_putovanje')
] 