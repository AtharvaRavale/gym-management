
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from datetime import datetime

# Home page view
def home(request):
    # Add some logic for messages if needed
    if request.method == "POST":
        # For example, if a user submits some form, you can add a success message
        messages.success(request, "Welcome to GymPro! Start your fitness journey today.")
    
    # Get the current year for the footer
    # current_year = datetime.now().year
    
    # Render the home template with context data
    return render(request, 'home/home.html')
        # 'current_year': current_year
    
