from rest_framework.viewsets import ModelViewSet
from ..models import Wishlist, WishListItem
from ..serializers import WishListSerializer, WishListItemSerializer

class WishListViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishListSerializer
    lookup_field = 'pk'

class WishListItemViewSet(ModelViewSet):
    queryset = WishListItem.objects.all()
    serializer_class = WishListItemSerializer
    lookup_field = 'pk'
