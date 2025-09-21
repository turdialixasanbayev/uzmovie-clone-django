from rest_framework import permissions, generics
from ..models.film import Film
from ..serializers.filmDetail import FilmDetailSerializer


class FilmDetailAPIView(generics.RetrieveAPIView):
    """
    A view film detail
    """

    queryset = Film.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FilmDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.select_related('category', 'country').prefetch_related('tags')
