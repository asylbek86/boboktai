from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from firebase_admin import auth as firebase_auth

from .serializers import RegisterSerializer, LoginSerializer
from apps.users.serializers import UserSerializer


User = get_user_model()


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        id_token = serializer.validated_data["id_token"]
        full_name = serializer.validated_data["full_name"]
        phone_number = serializer.validated_data["phone_number"]

        try:
            decoded = firebase_auth.verify_id_token(id_token)
        except Exception:
            return Response({"detail": "Invalid Firebase token"}, status=status.HTTP_401_UNAUTHORIZED)

        firebase_uid = decoded["uid"]

        user, created = User.objects.get_or_create(
            firebase_uid=firebase_uid,
            defaults={
                "full_name": full_name,
                "phone_number": phone_number,
                "is_active": True,
            },
        )

        if not created:
            updated = False
            if user.full_name != full_name:
                user.full_name = full_name
                updated = True
            if user.phone_number != phone_number:
                user.phone_number = phone_number
                updated = True
            if updated:
                user.save(update_fields=["full_name", "phone_number"])

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": UserSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        id_token = serializer.validated_data["id_token"]

        try:
            decoded = firebase_auth.verify_id_token(id_token)
        except Exception:
            return Response({"detail": "Invalid Firebase token"}, status=status.HTTP_401_UNAUTHORIZED)

        firebase_uid = decoded["uid"]

        try:
            user = User.objects.get(firebase_uid=firebase_uid, is_active=True)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": UserSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

