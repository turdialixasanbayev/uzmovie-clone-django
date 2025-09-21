from django.urls import path

from ..views.filmCreate import FilmCreateAPIView
from ..views.filmList import FilmListAPIView


urlpatterns = [
    path(
        'film_create/',
        FilmCreateAPIView.as_view(),
        name='film_create',
    ),
    path(
        'film_list/',
        FilmListAPIView.as_view(),
        name='film_list',
    ),
]
