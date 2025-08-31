from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    """
    Contact model
    """
    class SectionCategory(models.TextChoices):
        """
        Section categories for the Contact model
        """
        FILM = "film", "Film"
        TECHNICAL = "technical", "Technical"

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True, region="UZ", max_length=20)
    telegram_username = models.CharField(max_length=64, blank=True, null=True)
    section = models.CharField(
        max_length=20, choices=SectionCategory.choices, blank=True, null=True)
    subject = models.CharField(max_length=150, blank=True, null=True)
    message = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for the Contact model
        """
        ordering = ["-created_at"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self) -> str:
        """
        String representation of the Contact model
        """
        if self.subject:
            return f"{self.name} - {self.subject}"
        return f"{self.name}"
