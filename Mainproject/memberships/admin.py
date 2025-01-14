from django.contrib import admin
from .models import Membership,Trainer


# Register your models here.
admin.site.register([Membership,Trainer])