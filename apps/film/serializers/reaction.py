from rest_framework import serializers
from ..models import Reaction
from apps.users.serializers import CustomUserLCSerializer

class ReactionSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)
    class Meta:
        model = Reaction
        fields = '__all__'

        def create(self, validated_data):
            return Reaction.objects.create(**validated_data)
