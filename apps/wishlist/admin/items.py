from django.contrib import admin
from ..models import WishListItem


class WishListItemAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the WishListItem model.
    """
    model = WishListItem
    ordering = ('added_at',)
    list_per_page = 2
    date_hierarchy = 'added_at'
    list_display = ('id', 'wishlist', 'movie', 'added_at',)
    list_filter = ('added_at',)
    search_fields = ('movie__name',)
    autocomplete_fields = ("movie",)
    list_display_links = ('id', 'wishlist',)
    readonly_fields = ('added_at', 'id',)

admin.site.register(WishListItem, WishListItemAdmin)
