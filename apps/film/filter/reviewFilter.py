import django_filters as filter
from ..models import Review

class ReviewFilter(filter.FilterSet):
    user = filter.NumberFilter(
        field_name="user_id",
        lookup_expr="exact",
        label="User ID"
    )
    film = filter.NumberFilter(
        field_name="film_id",
        lookup_expr="exact",
        label="Film ID"
    )
    created_at = filter.DateFromToRangeFilter(
        field_name="created_at",
        label="Created Between"
    )
    updated_at = filter.DateFromToRangeFilter(
        field_name="updated_at",
        label="Updated Between"
    )

    class Meta:
        model = Review
        fields = ["user", "film", "created_at", "updated_at"]
