from django.db import models

from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
        db_index=True,
        limit_choices_to={'parent__isnull': True},
    )
    slug = models.SlugField(max_length=150, db_index=True, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
