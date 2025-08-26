from django.db import models
from apps.wishlist.models import Wishlist
from apps.film.models import Film


class WishListItem(models.Model):
    """
    Model representing an item in a user's wishlist.
    """
    wishlist = models.ForeignKey(
        to=Wishlist,
        on_delete=models.CASCADE,
        related_name="wishlist_items",
        verbose_name="Wishlist",
        help_text="The wishlist this item belongs to"
    )
    movie = models.ForeignKey(
        to=Film,
        on_delete=models.CASCADE,
        related_name="in_wishlists",
        verbose_name="Movie",
        help_text="The movie added to the wishlist"
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Added At",
        help_text="The date and time when the movie was added to the wishlist"
    )

    class Meta:
        """
        Meta options for the wishlist item model.
        """
        verbose_name = "Wishlist Item"
        verbose_name_plural = "Wishlist Items"
        ordering = ["-added_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["wishlist", "movie"],
                name="unique_wishlist_movie"
            )
        ]
        indexes = [
            models.Index(fields=["wishlist"]),
            models.Index(fields=["movie"]),
        ]

    def __str__(self) -> str:
        """
        Return a string representation of the wishlist item.
        """
        return f"{self.movie} in {self.wishlist}"
