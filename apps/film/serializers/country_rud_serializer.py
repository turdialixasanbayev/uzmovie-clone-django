from rest_framework import serializers
from ..models import Country


class CountryRUDAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
