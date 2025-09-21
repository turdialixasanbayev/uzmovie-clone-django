from rest_framework import serializers
from ..models import Film
from apps.category.serializers import CategoryLCSerializer, TagLCSerializer
from ..serializers.country_lc_serializer import CountryLCAPISerializer


class FilmDetailSerializer(serializers.ModelSerializer):
    tags = TagLCSerializer(many=True, read_only=True)
    country = CountryLCAPISerializer(read_only=True)
    category = CategoryLCSerializer(read_only=True)

    class Meta:
        model = Film
        fields = '__all__'
