from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, full_name, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The phone number must be set")
        phone_number = str(phone_number)
        user = self.model(phone_number=phone_number, full_name=full_name, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, full_name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone_number, full_name, password, **extra_fields)


class User(AbstractUser):
    username = None
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20, default="user")
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.full_name} ({self.phone_number})"

