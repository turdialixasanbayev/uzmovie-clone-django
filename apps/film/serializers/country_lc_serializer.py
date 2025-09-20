from rest_framework import serializers
from ..models import Country


class CountryLCAPISerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Country
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]

        def create(self, validated_data):
            return Country.objects.create(**validated_data)
