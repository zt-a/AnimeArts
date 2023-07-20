# Generated by Django 4.2.3 on 2023-07-20 12:22

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=255, verbose_name='Ваш Email')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратные связи',
                'ordering': ['-time_create', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AnimeArtModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='anime_images/', verbose_name='Картинка')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('genres', models.ManyToManyField(to='main.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
                'ordering': ['-time_create', 'id'],
            },
        ),
    ]