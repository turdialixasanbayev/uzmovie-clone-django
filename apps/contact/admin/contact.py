from django.contrib import admin

from ..models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    ordering = ("-created_at",)
    list_filter = ("section",)

    list_display = (
        "id",
        "name",
        "email",
        "phone_number",
        "telegram_username",
        "section",
        "subject",
        "created_at",
    )

    search_fields = ("name", "email", "phone_number", 'telegram_username',)
    readonly_fields = ('id', "created_at",)

    fieldsets = (
        ("Personal Information", {
            "classes": ("wide",),
            "fields": ("name", "email", "phone_number", "telegram_username",),
        }),
        ("Message Details", {
            "classes": ("wide",),
            "fields": ("section", "subject", "message",),
        }),
        ("Timestamps", {
            "classes": ("wide", 'collapse',),
            "fields": ("created_at",),
        }),
        ("ID", {
            "classes": ("wide", 'collapse',),
            "fields": ("id",),
        }),
    )
