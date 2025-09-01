from rest_framework import generics
from ..models import Category
from ..serializers import CategoryLCSerializer
from rest_framework import permissions
from ..filter import CategoryFilter


class CategoryLCView(generics.ListCreateAPIView):
    """
    List all categories with their details
    """

    queryset = Category.objects.all()
    serializer_class = CategoryLCSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    filterset_class = CategoryFilter

    def get_queryset(self):
        return self.queryset.select_related('parent')
