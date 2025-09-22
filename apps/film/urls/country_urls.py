from django.urls import path, include

from rest_framework import routers

from ..views import CountryLCAPIView, CountryRUDAPIView

from ..views import ReactionViewSet, ReviewViewSet


country_lc_api_as_view = CountryLCAPIView.as_view()
country_rud_api_as_view = CountryRUDAPIView.as_view()

router = routers.DefaultRouter()

router.register(r'reactions', ReactionViewSet, basename='reaction')
router.register(r'reviews', ReviewViewSet, basename='review')


urlpatterns = [
    path('countries/', country_lc_api_as_view, name='country-list'),
    path('countries/<int:pk>/', country_rud_api_as_view, name='country-detail'),

    path('', include(router.urls)),
]
