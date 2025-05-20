from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    ROLES = [
        ('ADMIN', 'Administrator'),
        ('USER', 'User')
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='USER')
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    preferred_channel = models.CharField(
        max_length=10,
        choices=[('email', 'Email'), ('mail', 'Mail')],
        default='email'
    )