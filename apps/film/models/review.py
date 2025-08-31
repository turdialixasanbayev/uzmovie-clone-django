from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()


class Review(models.Model):
    """
    Model representing a film review.
    """
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="review",
        help_text="The user who wrote this review",
        db_index=True
    )
    film = models.ForeignKey(
        to="film.Film",
        on_delete=models.CASCADE,
        related_name="reviews",
        help_text="The film that was reviewed",
        db_index=True
    )
    description = RichTextField(
        null=True,
        blank=True,
        help_text="Write your review about the film"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text="The date and time when the review was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_index=True,
        help_text="The date and time when the review was last updated"
    )

    def __str__(self) -> str:
        """
        Return a string representation of the review.
        """
        return f"Review by {self.user.username} on {self.film}"

    class Meta:
        """
        Meta options for the review model.
        """
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["film"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "film"],
                name="unique_user_film_review"
            )
        ]
