from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, alx_travel_app='home'),
]