import django_filters
from ..models import Category


class CategoryFilter(django_filters.FilterSet):
    """
    FilterSet for Category model
    """

    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains", label="Category Name"
    )
    parent = django_filters.NumberFilter(
        field_name="parent__id", lookup_expr="exact", label="Parent ID"
    )

    class Meta:
        model = Category
        fields = ["name", "parent"]
