from django.urls import path
from main.views import PutovanjeList
from main.views import PrijaveList
from main.views import PutovanjePrijaveList
from . import views

#app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('putovanja/', PutovanjeList.as_view()),
    path('prijave/', PrijaveList.as_view()),
    path('<putovanja>/', PutovanjePrijaveList.as_view()),
    path('putovanje/<int:putovanje_sifraPutovanja>/', views.PutovanjeDetailView.as_view(), name='putovanje_detail'),

]