from rest_framework import generics, permissions
from ..models import Film
from ..serializers import FilmUpdateSerializer

class FilmUpdateAPIView(generics.UpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmUpdateSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'slug'

    def get_queryset(self):
        return Film.objects.all().select_related('category', 'country').prefetch_related('tags').order_by('release_date')

    def perform_update(self, serializer):
        return super().perform_update(serializer)
