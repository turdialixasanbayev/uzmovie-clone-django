from rest_framework import serializers
from ..models import Wishlist, WishListItem

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"

class WishListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItem
        fields = "__all__"
