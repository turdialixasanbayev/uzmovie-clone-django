from rest_framework import serializers
from ..models import Category


class CategoryRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'parent',
            'slug',
            'image',
            'description',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id',
            'slug',
            'created_at',
            'updated_at'
        ]
