from rest_framework import permissions, viewsets
from ..serializers import ReviewSerializer
from ..models import Review
from ..filter import ReviewFilter

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_class = ReviewFilter
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    pagination_class = None
    ordering_fields = ['created_at']
    ordering = ['created_at']

    def get_queryset(self):
        return Review.objects.all().select_related('film', 'user').order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()
