from rest_framework import permissions, viewsets
from ..serializers import ReactionSerializer
from ..models import Reaction
from ..filter import ReactionFilter

class ReactionViewSet(viewsets.ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    filterset_class = ReactionFilter
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    pagination_class = None
    ordering_fields = ['created_at']
    ordering = ['created_at']

    def get_queryset(self):
        return self.queryset.select_related('film', 'user').order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()
