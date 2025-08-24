from django.contrib import admin
from ..models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Wishlist model.
    """
    model = Wishlist
    ordering = ('-created_at',)
    list_per_page = 10
    date_hierarchy = 'created_at'
    list_display = ('id', 'user', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('user__username',)
    autocomplete_fields = ("user",)
    list_display_links = ('id', 'user',)
    readonly_fields = ('created_at', 'items_count', 'id',)

admin.site.register(Wishlist, WishlistAdmin)
