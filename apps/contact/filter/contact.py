import django_filters
from ..models import Contact


class ContactFilter(django_filters.FilterSet):
    """
    FilterSet for the Contact model
    """
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="email", lookup_expr="icontains")
    phone_number = django_filters.CharFilter(field_name="phone_number", lookup_expr="icontains")
    telegram_username = django_filters.CharFilter(field_name="telegram_username", lookup_expr="icontains")
    section = django_filters.ChoiceFilter(field_name="section", choices=Contact.SectionCategory.choices)
    subject = django_filters.CharFilter(field_name="subject", lookup_expr="icontains")
    created_at = django_filters.DateFromToRangeFilter(field_name="created_at")

    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "phone_number",
            "telegram_username",
            "section",
            "subject",
            "created_at",
        ]
