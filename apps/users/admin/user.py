from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from ..models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Admin interface for the CustomUser model.
    """

    model = CustomUser

    list_display = ("username", "email", "first_name", "last_name", "gender", "birth_date", "is_staff", "is_active",)
    list_filter = ("gender", "is_staff", "is_active",)
    filter_horizontal = ()

    fieldsets = (
        (None, {"fields": ("username", "password",)}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "gender", "birth_date",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser",)}),
        ("Important dates", {"fields": ("last_login", "date_joined",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "gender", "birth_date", "is_staff", "is_active",),
        }),
    )

    search_fields = ("username", "email", "first_name", "last_name",)
    ordering = ("username",)
