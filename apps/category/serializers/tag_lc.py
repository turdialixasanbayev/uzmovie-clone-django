from rest_framework import serializers
from ..models import Tag


class TagLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
        }
