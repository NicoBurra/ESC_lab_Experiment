from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('experiment/<int:pk>/', views.experiment_detail, name='experiment_detail'),
    path('experiment/new/', views.create_experiment, name='create_experiment'),
    path('experiment/<int:pk>/accept/', views.accept_experiment, name='accept_experiment'),
]
