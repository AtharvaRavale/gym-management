from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the home page
    # Add other URL patterns here, such as for memberships, trainers, etc.
]
