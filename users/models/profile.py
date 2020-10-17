import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class ProfileManager(BaseUserManager):
    """Менеджер для создания пользователей."""

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Адрес электронной почты должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Создает и возвращает `Profile`."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Создает и возвращает пользователя с правами суперпользователя (администратора)."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class Profile(AbstractUser):
    """Профиль пользователя."""
    username = None
    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )
    patronymic = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Отчество',
    )
    phone = models.CharField(
        max_length=32,
        blank=True,
        verbose_name='Телефон',
    )
    city = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Город',
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        blank=True,
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ProfileManager()

    def __str__(self):
        return self.email

    def _generate_jwt_token(self):
        """Создает веб-токен JSON.
        В нем в котором хранится идентификатор этого пользователя и срок его действия составляет 60 дней в будущем.
        """
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    @property
    def token(self):
        """Получение JWT токена авторизации."""
        return self._generate_jwt_token()
