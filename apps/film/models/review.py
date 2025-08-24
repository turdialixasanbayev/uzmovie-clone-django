from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()


class Review(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='review_user')
    film = models.ForeignKey(to='film.Film', on_delete=models.CASCADE, related_name='review_film')
    description = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user} on {self.film}"
