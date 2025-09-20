from django.urls import path

from ..views import CountryLCAPIView, CountryRUDAPIView


country_lc_api_as_view = CountryLCAPIView.as_view()
country_rud_api_as_view = CountryRUDAPIView.as_view()


urlpatterns = [
    path('countries/', country_lc_api_as_view, name='country-list'),
    path('countries/<int:pk>/', country_rud_api_as_view, name='country-detail'),
]
