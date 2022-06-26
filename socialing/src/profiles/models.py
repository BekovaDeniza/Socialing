from django.contrib.auth.models import AbstractUser
from django.db import models


class UserNet(AbstractUser):
    """Custom user model
        """
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    )
    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=14)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    tg = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='other')
