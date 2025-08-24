from django.contrib import admin
from ..models import Film


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Film model.
    """
    model = Film
    ordering = ('-release_date',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'country__name',)
    filter_horizontal = ("tags",)
    autocomplete_fields = ("country",)
    date_hierarchy = 'release_date'
    list_display_links = ('id', 'name',)
    list_editable = ('slug',)
    list_per_page = 10
    list_display = (
        'id',
        'slug',
        'name',
        'image',
        'video',
        'category',
        'country',
        'trailer_link',
        'bot_link',
        'bot_code',
        'year',
        'language',
        'duration',
        'age_type',
        'release_date',
    )
    readonly_fields = (
        'id',
        'release_date',
        'views_count',
        'reviews_count',
        'likes_count',
        'dislikes_count',
        'rating',
    )
    list_filter = (
        'language',
        'year',
        'age_type',
        'release_date',
    )
