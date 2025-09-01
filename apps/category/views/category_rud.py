from rest_framework import generics
from ..models import Category
from ..serializers import CategoryRUDSerializer
from rest_framework import permissions


class CategoryRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRUDSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.select_related('parent')
