from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model with additional fields.

    user_permissions = None  # Disable user permissions
    groups = None  # Disable user groups
    """

    user_permissions = None
    groups = None

    class GenderChoices(models.TextChoices):
        """
        Gender choices for the user model.
        """
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        null=True,
        blank=True,
        help_text="Select your gender",
        db_index=True,
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        db_index=True,
        help_text="Enter your birth date",
    )

    def __str__(self) -> str:
        """
        Return the string representation of the user.
        """
        return self.get_full_name() or self.username

    class Meta:
        """
        Meta options for the user model.
        """
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
            models.Index(fields=['first_name']),
            models.Index(fields=['last_name']),
            models.Index(fields=['date_joined']),
            models.Index(fields=['gender']),
            models.Index(fields=['birth_date']),
        ]
