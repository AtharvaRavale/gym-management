from django.db import models

# Create your models here.

class Membership(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField() 
    # badge = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name




class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()  
    profile_picture = models.ImageField(upload_to='trainers/', blank=True, null=True)
    expertise = models.CharField(max_length=100)  
    # price_per_session = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
