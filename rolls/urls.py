from django.urls import path
from . import views  # Import the views from the current directory

urlpatterns = [
    path('', views.rolls, name='home'),  # Map the root URL to the rolls view
    path('contacts', views.contacts, name='contacts'),  # Map the root URL to the rolls view
    # You can add more paths here if needed
]