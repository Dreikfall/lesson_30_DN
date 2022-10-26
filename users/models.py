from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRole(models.Model):
    choices = [
        ('member', 'Пользователь'),
        ('admin', 'Админ'),
        ('moderator', 'Модератор')
    ]


class User(AbstractUser):
    role = models.CharField(choices=UserRole.choices, max_length=9, default='member')
    locations = models.ManyToManyField(Location)
    age = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'