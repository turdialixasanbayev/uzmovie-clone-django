from rest_framework import serializers
from ..models import CustomUser


class CustomUserRUDSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieve and update and delete CustomUser instances.
    """
    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = ['id', 'date_joined', 'last_login']
