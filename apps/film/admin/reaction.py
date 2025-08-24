from django.contrib import admin
from ..models import Reaction


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Reaction model.
    """
    model = Reaction
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
        'reaction',
        'created_at',
    )
    readonly_fields = (
        'id',
        'created_at',
    )
    list_filter = (
        'reaction',
        'created_at',
    )
