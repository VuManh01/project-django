# patients/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('', views.patients_list, name='patients_list'),
]
