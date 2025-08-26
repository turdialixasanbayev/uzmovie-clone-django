from django.db import models


class Country(models.Model):
    """
    Represents a country with its official name and ISO code.
    """

    name = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
        verbose_name="Country Name",
        help_text="The official name of the country (e.g., Uzbekistan)",
    )
    code = models.CharField(
        max_length=3,
        unique=True,
        db_index=True,
        verbose_name="Country Code",
        help_text="The ISO 3166-1 alpha-3 country code (e.g., UZB)",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when this country was added",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
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
        ]

    def __str__(self) -> str:
        """
        Return a string representation of the country.
        """
        return f"{self.name} ({self.code})"
