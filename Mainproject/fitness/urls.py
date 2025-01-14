from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls,name='admin'),
    
    # Account-related URLs
    path('accounts/', include('accounts.urls')),
    
    # Home page (index) - serves the homepage template
    path('', TemplateView.as_view(template_name="index.html"), name='home'),  # root URL maps to home page
    
    # App-specific URLs
    path('home/', include('home.urls')),             # Home page URLs from the 'home' app
    path('memberships/', include('memberships.urls')),  # Include your app's URL configuration here
    path('workout_plans/', include('workout_plans.urls')),  # Workout plans-related URLs
    #path('contact/', include('contact.urls')),  # Contact-related URLs
      # Include workout_plans URLs
   # path('trainers/', include('trainers.urls') ) , 
   # path('trainer_detail/', include('trainer_detail.urls') ) , 




]
