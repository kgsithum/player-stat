from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64,unique=True)
    date_of_birth = models.DateField(blank=True)
    is_active = models.BooleanField(default=True)
