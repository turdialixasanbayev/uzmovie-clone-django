import django_filters
from ..models import Country


class CountryFilter(django_filters.FilterSet):
    """
    FilterSet for Country model.
    Allows filtering by name (icontains), code (exact), 
    created_at range and updated_at range.
    """

    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains", label="Country name"
    )
    code = django_filters.CharFilter(
        field_name="code", lookup_expr="exact", label="Country code"
    )
    created_at = django_filters.DateFromToRangeFilter(
        field_name="created_at", label="Created date range"
    )
    updated_at = django_filters.DateFromToRangeFilter(
        field_name="updated_at", label="Updated date range"
    )

    class Meta:
        """
        Meta class for CountryFilter.
        Specifies the model and fields to be used for filtering.
        """
        model = Country
        fields = ["name", "code", "created_at", "updated_at"]
