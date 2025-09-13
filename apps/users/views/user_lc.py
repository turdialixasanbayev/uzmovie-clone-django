from rest_framework import generics, permissions
from ..serializers import CustomUserLCSerializer
from ..models import CustomUser
from ..filter import CustomUserFilter


class CustomUserLCAPIView(generics.ListCreateAPIView):
    """
    API view to list all users or create a new user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserLCSerializer
    permission_classes = [permissions.IsAdminUser]
    filterset_class = CustomUserFilter
    # pagination_class = None  # You can set your pagination class here

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return super().get_queryset().order_by('date_joined')
