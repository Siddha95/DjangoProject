from django.urls import path
from . import views  # Import the views from the current directory

urlpatterns = [
    path('', views.rolls)  # Map the root URL to the rolls view
    # You can add more paths here if needed
]