from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")

    creation_date = models.DateTimeField(auto_created=True, verbose_name="Дата создания")
    published_date = models.DateTimeField(verbose_name="Дата публикации")
    editing_date = models.DateTimeField(auto_created=True, verbose_name="Дата редактирования")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.URLField(verbose_name="Фото", default="http://placehold.it/900x300")
    tags = models.ManyToManyField('Tag', blank=True, verbose_name="Тег", related_name='posts')

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ['-published_date']


class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)


    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ['-name']
