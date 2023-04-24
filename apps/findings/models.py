from django.db import models
from django_editorjs import EditorJsField
from uuid import uuid4

from apps.common.models import AbstractBaseModel
from apps.users.models import User 


class Category(AbstractBaseModel):
    name = models.CharField(
        max_length=120, 
        verbose_name='Название', 
    )
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        related_name='children', 
        blank=True,
        null=True,
        verbose_name='Родительская категория'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Finding(AbstractBaseModel):
    name = models.CharField(
        max_length=120,
        verbose_name='Название'
    )
    description = EditorJsField(
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        verbose_name='Цена'
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='findings',
        verbose_name='Автор'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='findings',
        verbose_name='Категория'
    )
    is_active = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'Находка'
        verbose_name_plural = 'Находки'

    def __str__(self):
        return self.name


class Image(AbstractBaseModel):
    finding = models.ForeignKey(
        Finding, 
        on_delete=models.CASCADE, 
        related_name='images', 
        verbose_name='Картинки'
    )
    image = models.FileField(
        upload_to='static/images/%Y/%m/%d/',
        max_length=255
    )
    is_preview = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.finding
