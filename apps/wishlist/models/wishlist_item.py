from django.db import models
from apps.wishlist.models import Wishlist
from apps.film.models import Film as Movie


class WishListItem(models.Model):
    wishlist = models.ForeignKey(to=Wishlist, on_delete=models.CASCADE, related_name='items')
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, related_name='wishlist_items')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['wishlist', 'movie'], name='unique_wishlist_movie')
        ]

    def __str__(self):
        return f"WishListItem({self.wishlist}, {self.movie})"
