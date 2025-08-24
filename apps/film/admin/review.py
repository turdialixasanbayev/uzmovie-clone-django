from django.contrib import admin
from ..models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Review model.
    """
    model = Review
    ordering = ('-created_at',)
    search_fields = ('film__name', 'user__username',)
    autocomplete_fields = ("film", "user",)
    date_hierarchy = 'created_at'
    list_display_links = ('id', 'film',)
    list_per_page = 10
    list_display = (
        'id',
        'film',
        'user',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'created_at',
        'updated_at',
    )
