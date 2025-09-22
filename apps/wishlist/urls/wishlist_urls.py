from django.urls import include, path
from rest_framework import routers
from ..views import WishListViewSet, WishListItemViewSet

router = routers.DefaultRouter()
router.register(r'wishlist', WishListViewSet, basename='wishlist')
router.register(r'items', WishListItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls)),
]
