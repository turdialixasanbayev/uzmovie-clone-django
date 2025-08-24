from django.db import models


class Country(models.Model):
    """
    This is the Country model, representing a country with a name and code.
    """
    name = models.CharField(max_length=150, unique=True, db_index=True)
    code = models.CharField(max_length=3, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})"
