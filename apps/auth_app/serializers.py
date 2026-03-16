from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    id_token = serializers.CharField()
    full_name = serializers.CharField(max_length=150)
    phone_number = serializers.CharField(max_length=20)


class LoginSerializer(serializers.Serializer):
    id_token = serializers.CharField()

