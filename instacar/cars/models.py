from django.db import models
from django.utils import timezone

from users.models import UserProfile
from .validators import validate_year


class Car(models.Model):
    """Модель Машины"""
    make = models.CharField(
        max_length=100,
        verbose_name='Марка',
        blank=False,
        null=False
    )
    model = models.CharField(
        max_length=100,
        verbose_name='Модель',
        blank=False,
        null=False
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        validators=[validate_year],
        blank=False, null=False
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        related_name='cars'
    )

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class Comment(models.Model):
    """Модель Комментария"""
    content = models.TextField(
        verbose_name='Содержание комментария',
        blank=False, null=False
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания'
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Автомобиль',
        related_name='comments'
    )
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='comments'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created_at',)

    def __str__(self):
        return f"Комментарий от {self.author} к {self.car}"
