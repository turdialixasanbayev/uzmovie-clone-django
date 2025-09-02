import django_filters
from ..models import Tag


class TagFilter(django_filters.FilterSet):
    """
    FilterSet for Tag model
    """
    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
        label="Search by name"
    )

    class Meta:
        model = Tag
        fields = ["name"]
