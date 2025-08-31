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

    name = models.CharField(max_length=100, db_index=True, help_text="Full name of the contact person")
    email = models.EmailField(max_length=100, blank=True, null=True, db_index=True, help_text="Email address of the contact person")
    phone_number = PhoneNumberField(blank=True, null=True, region="UZ", max_length=20, db_index=True, help_text="Phone number of the contact person")
    telegram_username = models.CharField(max_length=64, blank=True, null=True, db_index=True, help_text="Telegram username of the contact person")
    section = models.CharField(
        max_length=20, choices=SectionCategory.choices, blank=True, null=True, db_index=True, help_text="Section category of the contact")
    subject = models.CharField(max_length=150, blank=True, null=True, db_index=True, help_text="Subject of the contact message")
    message = RichTextField(blank=True, null=True, help_text="Message from the contact person")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for the Contact model
        """
        ordering = ["-created_at"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['email']),
            models.Index(fields=['phone_number']),
            models.Index(fields=['telegram_username']),
            models.Index(fields=['section']),
            models.Index(fields=['subject']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self) -> str:
        """
        String representation of the Contact model
        """
        if self.subject:
            return f"{self.name} - {self.subject}"
        return f"{self.name}"
