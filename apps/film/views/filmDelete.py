from rest_framework import permissions, generics

from ..models import Film
from ..serializers import FilmDeleteSerializer


class FilmDeleteAPIView(generics.DestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmDeleteSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.select_related('category', 'country').prefetch_related('tags').order_by('release_date')

    def perform_destroy(self, instance):
        instance.delete()
