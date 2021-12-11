from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Character(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    death_year = models.CharField(max_length=64)
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name