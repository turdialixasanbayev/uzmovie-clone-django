from django.contrib import admin

from ..models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin panel for managing contact messages.
    """

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
        "updated_at",
    )

    search_fields = ("name", "email", "phone_number",)
    readonly_fields = ('id', "created_at", "updated_at")

    fieldsets = (
        ("Personal Information", {
            "fields": ("name", "email", "phone_number", "telegram_username",),
        }),
        ("Message Details", {
            "fields": ("section", "subject", "message",),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at",),
            "classes": ("collapse",),
        }),
        ("ID", {
            "fields": ("id",),
            "classes": ("collapse",),
        }),
    )
