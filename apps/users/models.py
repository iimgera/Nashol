from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from apps.common.constants import UserType
from apps.common.models import AbstractBaseModel


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password,  **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    is_admin = models.BooleanField(
        default=False, verbose_name='Admin'
    )

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(AbstractBaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users'
    )
    number = models.CharField(max_length=60, verbose_name='Номер телефона')
    type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.CONSUMER,
        verbose_name='Тип пользователя'
    )
    # POSTGIS
    geo = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Геолокация'
    )
    rating = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name='Рейтинг'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username} Тел: {self.number}'

    def clean(self):
        super().clean()
        if self.type == UserType.PRODUCER:
            if self.geo is None:
                raise validators.ValidationError(
                    'Геолокация обязательна'
                )

            if self.rating is None:
                raise validators.ValidationError(
                    'Рейтинг обязателен'
                )
