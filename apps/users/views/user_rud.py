from rest_framework import generics, permissions
from ..models import CustomUser
from ..serializers import CustomUserRUDSerializer


class CustomUserRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a user instance.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRUDSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'  # or 'id' depending on your URL configuration

    def get_queryset(self):
        return super().get_queryset().order_by('date_joined')
    
    def perform_update(self, serializer):
        serializer.save()
    
    def perform_destroy(self, instance):
        instance.delete()
