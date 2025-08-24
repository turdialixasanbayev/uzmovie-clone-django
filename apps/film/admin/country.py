from django.contrib import admin
from ..models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Country model.
    """
    model = Country
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 5
    list_display = (
        'id',
        'name',
        'code',
        'created_at',
        'updated_at',
    )
    search_fields = (
        "name",
        'code',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )
    list_display_links = (
        'id',
        'name',
    )
    list_filter = (
        'created_at',
        'updated_at',
    )
