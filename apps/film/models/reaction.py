from django.db import models
from django.conf import settings


class Reaction(models.Model):
    LIKE = 1
    DISLIKE = -1

    REACTION_CHOICES = (
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    )
    film = models.ForeignKey('film.Film', on_delete=models.CASCADE, related_name="reactions")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="film_reactions")
    reaction = models.SmallIntegerField(choices=REACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'film'],
                name='unique_reaction',
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.film} - {self.get_reaction_display()}"
