from django.db import models

from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


class SectionCategory(models.TextChoices):
    FILM = "film", "Film"
    TECHNICAL = "technical", "Technical"


class Contact(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=150, null=True, blank=True, db_index=True)
    phone_number = PhoneNumberField(max_length=15, blank=True, null=True, db_index=True, region="UZ")
    telegram_username = models.URLField(max_length=264, blank=True, null=True, db_index=True)
    section = models.CharField(max_length=100, blank=True, null=True, db_index=True, choices=SectionCategory.choices)
    subject = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    message = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
