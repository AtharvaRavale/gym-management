
# Create your models here.
from django.db import models

class WorkoutPlan(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    



# class WorkoutPlan_details(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
    

#     def __str__(self):
#         return self.title

