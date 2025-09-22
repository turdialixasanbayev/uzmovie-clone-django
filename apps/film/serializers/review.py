from rest_framework import serializers
from ..models import Review
from apps.users.serializers import CustomUserLCSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

        def create(self, validated_data):
            return Review.objects.create(**validated_data)
