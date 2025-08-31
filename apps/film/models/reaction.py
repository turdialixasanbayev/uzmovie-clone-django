from django.db import models
from django.conf import settings


class Reaction(models.Model):
    """
    Model representing a user's reaction to a film.
    """
    class ReactionType(models.IntegerChoices):
        LIKE = 1, "Like"
        DISLIKE = -1, "Dislike"

    film = models.ForeignKey(
        "film.Film",
        on_delete=models.CASCADE,
        related_name="reactions",
        help_text="The film that the user reacted to",
        db_index=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reaction",
        help_text="The user who reacted to the film",
        db_index=True,
    )
    reaction = models.SmallIntegerField(
        choices=ReactionType.choices,
        help_text="User's reaction to the film (like or dislike)",
        db_index=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text="The date and time when the reaction was created",
    )

    class Meta:
        verbose_name = "Reaction"
        verbose_name_plural = "Reactions"
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "film"],
                name="unique_user_film_reaction",
            )
        ]
        indexes = [
            models.Index(fields=["film"]),
            models.Index(fields=["user"]),
            models.Index(fields=["reaction"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self) -> str:
        return f"{self.user.username} → {self.film} ({self.get_reaction_display()})"
