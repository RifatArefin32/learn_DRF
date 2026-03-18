from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male')

    def __str__(self):
        # Fall back to username if full name isn't set (admin listviews often use __str__)
        return self.get_full_name() or self.username