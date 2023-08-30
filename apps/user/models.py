from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    title = models.CharField(max_length=100, null=True, blank=True, help_text='Your profession') #either allow null or provide default
    bio = models.TextField(default='', null=True, blank=True)
    
