from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    nat_id = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10,null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
