from rest_framework import serializers
from ..models import Film


class FilmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        read_only_fields = [
            'id',
            'release_date',
        ]
