from django.db import models

from django.contrib.auth.models import AbstractUser

class GamePassed(models.Model):
    game_name = models.CharField(max_length=255, verbose_name="Название игры", null=True, blank=True)
    hours_played = models.PositiveIntegerField(verbose_name="Часы, потраченные на прохождение", null=True, blank=True)
    developer = models.CharField(max_length=255, verbose_name="Разработчик", null=True, blank=True)

    def __str__(self):
        return self.game_name

    class Meta:
        verbose_name = "Пройденные игры"
        verbose_name_plural = "Пройденные игры"

class Users(AbstractUser):
    games = models.ManyToManyField(to=GamePassed, related_name='users', default=None, blank=True, verbose_name="Игры, которые прошел")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
