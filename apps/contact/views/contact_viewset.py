from rest_framework import viewsets, permissions
from ..filter import ContactFilter
from ..models import Contact
from ..serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing contact instances.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = ContactFilter
    lookup_field = 'pk'
    ordering = ['created_at']
    # pagination_class = None  # Disable pagination for this viewset
    # lookup_url_kwarg = 'contact_pk' # Custom URL kwarg for lookup field

    def get_queryset(self):
        return self.queryset
