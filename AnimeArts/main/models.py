from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('genres', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['id']


# def get_anime_image_path(instance, filename):
#     genres = '-'.join([genre.name for genre in instance.genres.all()])
#     # user = instance.user.username  # Предполагаем, что у объекта Anime есть связь с пользовательским профилем (UserProfile) через поле "user".
#     return f'anime_images/{genres}/{filename}'



class AnimeArtModel(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(verbose_name='Описание', blank=True, max_length=255)
    genres = models.ManyToManyField(Genre, verbose_name='Жанр')
    image = models.ImageField(verbose_name='Картинка', upload_to='anime_images/')

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('AnimeArts', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['-time_create', 'id']


class ContactUsModel(models.Model):
    name = models.CharField(verbose_name='Ваше имя', max_length=255)
    email = models.EmailField(verbose_name='Ваш Email', max_length=255)
    message = models.TextField(verbose_name='Сообщение')


    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'
        ordering = ['-time_create', 'id']
