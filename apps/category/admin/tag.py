from django.contrib import admin

from ..models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    ordering = ('-name',)
    list_display = ("id", "name",)
    search_fields = ("name",)
    readonly_fields = ('id',)
    list_per_page = 10
    list_display_links = ("id", "name",)

    fieldsets = (
        ("Tag Information", {
            "fields": ("name",),
            "classes": ("wide",),
            "description": "Enter a unique name for the tag.",
        }),
        ("ID", {
            "fields": ("id",),
            "classes": ("wide", 'collapse',),
            "description": "This field is automatically generated.",
        }),
    )
