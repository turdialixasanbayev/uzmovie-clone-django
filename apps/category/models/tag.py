from django.db import models


class Tag(models.Model):
    """
    Tag model
    """
    name = models.CharField(max_length=150, unique=True, db_index=True, help_text="Enter the tag name")

    class Meta:
        """
        Meta class
        """
        ordering = ['name']
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self) -> str:
        """
        __str__ method
        """
        return f"{self.name}"
