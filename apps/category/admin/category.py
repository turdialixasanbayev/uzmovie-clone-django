from django.contrib import admin

from ..models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Category model.
    """

    model = Categorya
    ordering = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('id', 'created_at', 'updated_at',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    list_display_links = ('id', 'name',)
    list_editable = ('slug',)
    list_per_page = 10
    list_display = ('id', 'name', 'slug', 'parent', 'image', 'created_at', 'updated_at',)

    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "parent", "slug",),
            "description": "Name and slug of the category. If no slug is provided, it will be generated automatically.",
            "classes": ("wide",),
        }),
        ("Media", {
            "fields": ("image",),
            "classes": ("wide",),
            "description": "Upload an image representing this category."
        }),
        ("Content", {
            "fields": ("description",),
            "classes": ("wide",),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at",),
            "classes": ("wide",),
        }),
        ("ID", {
            "fields": ("id",),
            "classes": ("wide", 'collapse',),
        }),
    )
