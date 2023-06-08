from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Custom fields for User model
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True)
    doate_of_birth =models.DateField(null=True)

class PasswordEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    website_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    encrypted_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.website_name

