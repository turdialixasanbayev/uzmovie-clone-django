from rest_framework import generics, permissions

from ..models import Country
from ..serializers import CountryRUDAPISerializer


class CountryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryRUDAPISerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'pk' # You can change this to 'id' or any other field if needed

    def get_queryset(self):
        """
        Optionally restricts the returned countries to a given user,
        by filtering against a `username` query parameter in the URL.
        """

        queryset = super().get_queryset()

        return queryset.order_by('created_at')  # Order by created at descending

    def perform_update(self, serializer):
        """
        Override to handle any additional logic during update if needed.
        """

        serializer.save()

    def perform_destroy(self, instance):
        """Override to handle any additional logic during delete if needed."""

        instance.delete()
