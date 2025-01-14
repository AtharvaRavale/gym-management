from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_plans, name='workout_plans'),  # List of all workout plans
    # path('<int:plan_id>/', views.workout_plan_detail, name='workout_plan_detail'),  # Detail view for a specific plan
]
