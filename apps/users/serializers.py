from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name", "phone_number", "role", "is_active", "date_joined"]
        read_only_fields = ["id", "role", "is_active", "date_joined"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["full_name", "phone_number", "role", "is_active"]

