from rest_framework import (
    generics,
    permissions,
)

from ..models import Country
from ..serializers import CountryLCAPISerializer
from ..filter import CountryFilter


class CountryLCAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of countries.
    Supports filtering by name, code, created_at range, and updated_at range.
    """

    queryset = Country.objects.all()
    serializer_class = CountryLCAPISerializer
    permission_classes = [permissions.IsAdminUser]
    filterset_class = CountryFilter
    pagination_class = None  # Disable pagination to return all results

    def get_queryset(self):
        """
        Optionally restricts the returned countries to a given user,
        by filtering against a `username` query parameter in the URL.
        """

        queryset = super().get_queryset()

        return queryset.order_by('created_at')  # Order by created at descending

    def perform_create(self, serializer):
        """Save the new country instance."""

        serializer.save()
