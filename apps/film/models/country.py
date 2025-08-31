from django.db import models


class Country(models.Model):
    """
    Represents a country with its official name and ISO code.
    """

    name = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
        help_text="The official name of the country (e.g., Uzbekistan)",
    )
    code = models.CharField(
        max_length=3,
        unique=True,
        db_index=True,
        help_text="The ISO 3166-1 alpha-3 country code (e.g., UZB)",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text="The date and time when this country was added",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_index=True,
        help_text="The date and time when this country was last updated",
    )

    class Meta:
        """
        Meta options for the country model.
        """
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["code"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
        ]

    def __str__(self) -> str:
        """
        Return a string representation of the country.
        """
        return f"{self.name} ({self.code})"
