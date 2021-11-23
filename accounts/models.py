from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255,verbose_name="Email Address")
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    age = models.IntegerField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','age']

    

    def __str__(self) -> str:
        return self.email