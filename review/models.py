from django.db import models
from django.urls import reverse

from loginer.models import Users

class Genre(models.Model):
    genre_name = models.CharField(max_length=255, verbose_name="Название жанра")

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name = "Жанры"
        verbose_name_plural = "Жанры"


class AgeCategory(models.Model):
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")

    def __str__(self):
        return str(self.age)

    class Meta:
        verbose_name = "Возрастная категория"
        verbose_name_plural = "Возрастная категория"


class Developer(models.Model):
    developer_name = models.CharField(max_length=255, verbose_name="Имя разработчика")

    def __str__(self):
        return self.developer_name

    class Meta:
        verbose_name = "Разработчики"
        verbose_name_plural = "Разработчики"

class Review(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя пользователя")
    rate = models.SmallIntegerField(verbose_name="Оценка")
    full_review = models.TextField(verbose_name="Полный текст отзыва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"

class Game(models.Model):
    game_name = models.CharField(max_length=255, verbose_name="Название игры")
    genre = models.ForeignKey(to=Genre, on_delete=models.CASCADE)
    age = models.ForeignKey(to=AgeCategory, on_delete=models.CASCADE)
    developer = models.ForeignKey(to=Developer, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Описание игры", default="Игра")
    img = models.ImageField(upload_to="game_img", verbose_name="Фото игры")
    reviews = models.ManyToManyField(Review, verbose_name="Отзывы", related_name="games", blank=True)
    users = models.ManyToManyField(Users, related_name='favorite_games', blank=True, verbose_name="Избранное")


    def __str__(self):
        return self.game_name

    class Meta:
        verbose_name = "Игры"
        verbose_name_plural = "Игры"

    def get_absolute_url(self):
        return reverse('review:game', kwargs={'id' : self.pk})






