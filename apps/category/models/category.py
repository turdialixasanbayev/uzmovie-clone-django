from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=150, unique=True, db_index=True, help_text="Enter the category name")
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
        limit_choices_to={'parent__isnull': True},
        db_index=True,
        help_text="Select a parent category (if any)"
    )
    slug = models.SlugField(max_length=155, unique=True, blank=True, null=True, db_index=True, help_text="Auto-generated from the name")
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class
        """
        ordering = ['name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
            models.Index(fields=['parent']),
        ]

    def save(self, *args, **kwargs):
        """
        save method for slug
        """
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """
        __str__ method
        """
        if self.parent:
            return f"{self.parent.name} → {self.name}"
        return f"{self.name}"
