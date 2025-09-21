from rest_framework import permissions, generics
from ..models.film import Film
from ..serializers.filmList import FilmListSerializer
from ..filter import FilmFilter


class FilmListAPIView(generics.ListAPIView):
    """
    A view film list
    """

    queryset = Film.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FilmListSerializer
    filterset_class = FilmFilter
    # pagination_class = None

    def get_queryset(self):
        return self.queryset.select_related('category', 'country').prefetch_related('tags').order_by('release_date')
