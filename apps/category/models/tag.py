from django.db import models


class Tag(models.Model):
    """
    Tag model
    """
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        """
        Meta class
        """
        ordering = ['name']
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self) -> str:
        """
        __str__ method
        """
        return f"{self.name}"
