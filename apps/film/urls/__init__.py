from django.urls import  include, path


urlpatterns = [
    path(
        '',
        include('apps.film.urls.country_urls'),
    ),
    path(
        '',
        include('apps.film.urls.film_urls'),
    ),
]
