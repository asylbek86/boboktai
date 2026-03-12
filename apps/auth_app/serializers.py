from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name", "phone_number"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        # Temporary simple registration without SMS code
        user, _ = User.objects.get_or_create(
            phone_number=validated_data["phone_number"],
            defaults={
                "full_name": validated_data["full_name"],
            },
        )
        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

