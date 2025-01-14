from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class Membership(models.Model):
    membership_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
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


class MembershipPurchase(models.Model):
    purchase_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='membership_purchases')
    membership = models.ForeignKey('Membership', on_delete=models.CASCADE)
    purchase_date = models.DateField()
    start_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.membership.name}"




# class Payment(models.Model):
#     transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

#     def __str__(self):
#         return f"{self.user.username} - {self.membership.name} - {self.status}"
