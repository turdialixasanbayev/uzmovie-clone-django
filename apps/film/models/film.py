from django.db import models
from django.apps import apps
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
import uuid


class Film(models.Model):
    class LANGUAGE(models.TextChoices):
        EN = 'EN', 'English'
        RU = 'RU', 'Russian'
        TR = 'TR', 'Turkish'
        UZ = 'UZ', 'Uzbek'

    class AGE_TYPE(models.IntegerChoices):
        ZERO = 0, '0+'
        SIX = 6, '6+'
        TWELVE = 12, '12+'
        SIXTEEN = 16, '16+'
        EIGHTEEN = 18, '18+'

    name = models.CharField(max_length=350, unique=True, db_index=True)
    slug = models.SlugField(max_length=450, unique=True,
                            null=True, blank=True, db_index=True)
    image = models.ImageField(upload_to='films', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    category = models.ForeignKey(
        to='category.Category', on_delete=models.CASCADE, related_name='film_category')
    tags = models.ManyToManyField(
        to='category.Tag', related_name='film_tags', blank=True)
    country = models.ForeignKey(
        to='film.Country', on_delete=models.CASCADE, related_name='film_country')
    description = RichTextField(null=True, blank=True)
    trailer_link = models.URLField(
        max_length=300, unique=True, null=True, blank=True)
    bot_link = models.URLField(max_length=300, null=True, blank=True)
    bot_code = models.CharField(
        max_length=10, unique=True, null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGE.choices, default=LANGUAGE.UZ)
    duration = models.DurationField(null=True, blank=True)
    age_type = models.IntegerField(choices=AGE_TYPE.choices, default=AGE_TYPE.ZERO)
    views = models.PositiveIntegerField(default=0)
    release_date = models.DateTimeField(auto_now_add=True)

    @property
    def views_count(self) -> int:
        return self.views or 0

    @property
    def reviews_count(self) -> int:
        return self.review_film.count() or 0

    @property
    def likes_count(self) -> int:
        Reaction = apps.get_model('film', 'Reaction')
        return self.reactions.filter(reaction=Reaction.LIKE).count() or 0

    @property
    def dislikes_count(self) -> int:
        Reaction = apps.get_model('film', 'Reaction')
        return self.reactions.filter(reaction=Reaction.DISLIKE).count() or 0

    @property
    def rating(self) -> int:
        return self.likes_count - self.dislikes_count

    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse('film_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            uuid_slug = f"{uuid.uuid4().hex[:8]}"
            date_slug = f"{timezone.now().strftime('%Y-%m-%d-%H-%M-%S')}"
            self.slug = f"{base_slug}-{uuid_slug}-{date_slug}"
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-release_date']
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def __str__(self):
        return f"{self.name}"
