from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Make sure views.home exists
]
