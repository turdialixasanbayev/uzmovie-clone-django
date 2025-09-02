from rest_framework import generics
from ..models import Tag
from ..serializers import TagRUDSerializer
from rest_framework import permissions


class TagRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a tag instance.
    """
    queryset = Tag.objects.all()
    serializer_class = TagRUDSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
