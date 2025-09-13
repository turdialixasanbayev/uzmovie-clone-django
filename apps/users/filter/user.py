import django_filters as filter
from ..models import CustomUser


class CustomUserFilter(filter.FilterSet):
    """
    FilterSet for CustomUser model
    """
    # Range filter for birth_date
    birth_date = filter.DateFromToRangeFilter(
        field_name="birth_date",
        label="Birth date (range)"
    )

    # Case-insensitive search filters
    first_name = filter.CharFilter(
        field_name="first_name",
        lookup_expr="icontains",
        label="First name (search)"
    )
    last_name = filter.CharFilter(
        field_name="last_name",
        lookup_expr="icontains",
        label="Last name (search)"
    )
    username = filter.CharFilter(
        field_name="username",
        lookup_expr="icontains",
        label="Username (search)"
    )
    email = filter.CharFilter(
        field_name="email",
        lookup_expr="icontains",
        label="Email (search)"
    )

    class Meta:
        model = CustomUser
        fields = {
            "gender": ["exact"],
            "birth_date": ["exact"],
            "date_joined": ["exact", "year__gt", "year__lt"],
            "is_active": ["exact"],
            "is_staff": ["exact"],
            "is_superuser": ["exact"],
        }
