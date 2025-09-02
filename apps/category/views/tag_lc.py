from rest_framework import generics
from ..models import Tag
from ..serializers import TagLCSerializer
from ..filter import TagFilter
from rest_framework import permissions


class TagLCView(generics.ListCreateAPIView):
    """
    View to list and create tags.
    """
    queryset = Tag.objects.all()
    serializer_class = TagLCSerializer
    filterset_class = TagFilter
    permission_classes = [permissions.IsAuthenticated]
    # pagination_class = None  # Disable pagination
