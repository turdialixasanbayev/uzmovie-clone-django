from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
