from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Wishlist(models.Model):
    """
    Model representing a user's wishlist.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="wishlist",
        help_text="The user who owns this wishlist"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the wishlist was created"
    )

    @property
    def items_count(self) -> int:
        """Returns the number of items in the wishlist."""
        return self.wishlist_items.count()

    def __str__(self) -> str:
        """
        Return a string representation of the wishlist.
        """
        return f"Wishlist of {self.user.get_full_name() or self.user.username}"

    class Meta:
        """
        Meta options for the wishlist model.
        """
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user"]),
        ]
