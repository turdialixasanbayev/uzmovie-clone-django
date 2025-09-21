from rest_framework import generics, permissions
from ..models import Film
from ..serializers import FilmCreateSerializer


class FilmCreateAPIView(generics.CreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmCreateSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Film.objects.all().select_related('category', 'country').prefetch_related('tags').order_by('release_date')
    
    def perform_create(self, serializer):
        serializer.save()
