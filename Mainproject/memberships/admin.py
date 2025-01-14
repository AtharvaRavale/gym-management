from django.contrib import admin
from .models import Membership,Trainer,MembershipPurchase


# Register your models here.
admin.site.register([Membership,Trainer,MembershipPurchase])