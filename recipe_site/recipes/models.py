from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя категории')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Категории"

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preparation_steps = models.TextField(verbose_name='Ингредиенты')
    cooking_time = models.IntegerField(verbose_name='Время приготовления')  # в минутах
    image = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    categories = models.ManyToManyField(Category, related_name='recipes', verbose_name='Категории')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Рецепты"
