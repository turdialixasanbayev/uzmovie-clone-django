from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist_user')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def items_count(self):
        return self.items.count()

    def __str__(self):
        return f"Wishlist of {self.user.username}"
