from django.db import models
from django.contrib.auth.models import AbstractUser
from instacar.constants import EMAIL_MAX_LENGHT


class UserProfile(AbstractUser):
    """Модель Пользователя"""
    email = models.EmailField(max_length=EMAIL_MAX_LENGHT, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()
