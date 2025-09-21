from django.urls import path

from ..views.filmCreate import FilmCreateAPIView
from ..views.filmList import FilmListAPIView
from ..views.filmDelete import FilmDeleteAPIView
from ..views.filmDetail import FilmDetailAPIView
from ..views.filmUpdate import FilmUpdateAPIView


film_update_as_view = FilmUpdateAPIView.as_view()


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
    path(
        'film_delete/<slug:slug>/',
        FilmDeleteAPIView.as_view(),
        name='film_delete',
    ),
    path(
        'film_detail/<slug:slug>/',
        FilmDetailAPIView.as_view(),
        name='film_detail',
    ),
    path(
        'film_update/<slug:slug>/',
        film_update_as_view,
        name='film_update',
    ),
]
