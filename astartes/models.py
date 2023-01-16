from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Marine(models.Model):
    title = models.CharField(max_length=64,help_text='marine name',default='blood ravens')
    region = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    region = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.title
    
