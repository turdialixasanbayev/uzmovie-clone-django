from django.db import models
from django.apps import apps
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
import uuid


class Film(models.Model):
    """
    Represents a film with metadata including category, country, tags,
    description, media, and user interactions.
    """

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

    P = (
        (0, '240p'),
        (1, '360p'),
        (2, '480p'),
        (3, '720p'),
        (4, '1080p'),
        (5, '4K' ),
    )

    name = models.CharField(
        max_length=350,
        unique=True,
        db_index=True,
        help_text="The official title of the film",
    )
    slug = models.SlugField(
        max_length=450,
        unique=True,
        blank=True,
        null=True,
        db_index=True,
        help_text="Unique slug generated from the film name",
    )
    image = models.ImageField(
        upload_to="films",
        null=True,
        blank=True,
        help_text="Film poster or cover image",
    )
    video = models.FileField(
        upload_to="videos",
        null=True,
        blank=True,
        help_text="Optional full video file",
    )
    category = models.ForeignKey(
        to="category.Category",
        on_delete=models.CASCADE,
        related_name="films",
        db_index=True,
        help_text="The category this film belongs to",
    )
    tags = models.ManyToManyField(
        to="category.Tag",
        related_name="film",
        blank=True,
        help_text="Tags associated with this film",
    )
    country = models.ForeignKey(
        to="film.Country",
        on_delete=models.CASCADE,
        related_name="film_country",
        db_index=True,
        help_text="Country where the film was produced",
    )
    description = RichTextField(
        null=True,
        blank=True,
        help_text="Detailed description or synopsis of the film",
    )
    trailer_link = models.URLField(
        max_length=300,
        unique=True,
        null=True,
        blank=True,
        db_index=True,
        help_text="YouTube or other video platform trailer URL",
    )
    bot_link = models.URLField(
        max_length=300,
        null=True,
        blank=True,
        db_index=True,
        help_text="Telegram bot link to access the film",
    )
    bot_code = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True,
        db_index=True,
        help_text="Unique bot access code for the film",
    )
    year = models.PositiveIntegerField(
        null=True,
        blank=True,
        db_index=True,
        help_text="The year the film was released",
    )
    language = models.CharField(
        max_length=2,
        choices=LANGUAGE.choices,
        default=LANGUAGE.UZ,
        db_index=True,
        help_text="Main language of the film",
    )
    duration = models.DurationField(
        null=True,
        blank=True,
        db_index=True,
        help_text="Film duration in HH:MM:SS",
    )
    age_type = models.IntegerField(
        choices=AGE_TYPE.choices,
        default=AGE_TYPE.ZERO,
        db_index=True,
        help_text="Minimum recommended viewer age",
    )
    views = models.PositiveIntegerField(
        default=0,
        db_index=True,
        help_text="Total number of views",
    )
    release_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text="The date and time when the film was added to the system",
    )

    p = models.IntegerField(
        choices=P,
        default=2,
        db_index=True,
        help_text="Video quality of the film",
    )

    @property
    def views_count(self) -> int:
        """
        Return the number of views for this film.
        """
        return self.views

    @property
    def reviews_count(self) -> int:
        """
        Return the number of reviews for this film.
        """
        return self.reviews.count()

    @property
    def likes_count(self) -> int:
        """Return the number of likes for this film."""
        Reaction = apps.get_model('film', 'Reaction')
        return self.reactions.filter(
            reaction=Reaction.ReactionType.LIKE
        ).count()

    @property
    def dislikes_count(self) -> int:
        """Return the number of dislikes for this film."""
        Reaction = apps.get_model('film', 'Reaction')
        return self.reactions.filter(
            reaction=Reaction.ReactionType.DISLIKE
        ).count()

    @property
    def rating(self) -> int:
        """
        Return the rating for this film.
        """
        return self.likes_count - self.dislikes_count

    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse('film_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """
        Save the film instance, generating a slug if it doesn't exist.
        """
        if not self.slug:
            base_slug = slugify(self.name)
            uuid_slug = f"{uuid.uuid4().hex[:8]}"
            date_slug = f"{timezone.now().strftime('%Y-%m-%d-%H-%M-%S')}"
            self.slug = f"{base_slug}-{uuid_slug}-{date_slug}"
        super().save(*args, **kwargs)

    class Meta:
        """
        Meta options for the film model.
        """
        ordering = ['-release_date']
        verbose_name = 'Film'
        verbose_name_plural = 'Films'
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["year"]),
            models.Index(fields=["release_date"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["category"]),
            models.Index(fields=["country"]),
            models.Index(fields=["trailer_link"]),
            models.Index(fields=["bot_link"]),
            models.Index(fields=["bot_code"]),
            models.Index(fields=["language"]),
            models.Index(fields=["duration"]),
            models.Index(fields=["age_type"]),
            models.Index(fields=["views"]),
            models.Index(fields=["p"]),
        ]

    def __str__(self) -> str:
        """
        Return a string representation of the film.
        """
        return f"{self.name}"
