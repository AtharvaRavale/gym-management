# Create your views here.
from django.shortcuts import render
from .models import WorkoutPlan
from django.contrib.auth.decorators import login_required


# View for displaying all workout plans
@login_required
def workout_plans(request):
    plans = WorkoutPlan.objects.all()  # Fetch all workout plans from the database
    return render(request, 'workout_plans/workout_plans_list.html', {'plans': plans})

# View for displaying details of a specific workout plan
# def workout_plan_detail(request, plan_id):
#     plan = WorkoutPlan_details.objects.all()  # Fetch specific plan or return 404
#     return render(request, 'workout_plans/workout_plan_detail.html', {'plan': plan})
