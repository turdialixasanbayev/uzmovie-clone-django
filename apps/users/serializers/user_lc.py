from rest_framework import serializers
from ..models import CustomUser


class CustomUserLCSerializer(serializers.ModelSerializer):
    """
    Serializer for listing and creating CustomUser instances.
    """
    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = ['id', 'date_joined', 'last_login']
