from django.urls import path
from . import views  # Import the views from your app

urlpatterns = [
    path('memberships/', views.memberships, name='memberships'),  # URL for Memberships page
    path('trainers/', views.trainers, name='trainers'),
    
    # URL pattern for the trainer detail view
    path('trainer/<int:trainer_id>/', views.trainer_detail, name='trainer_detail'),
]
