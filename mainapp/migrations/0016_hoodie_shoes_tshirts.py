# Generated by Django 2.1.11 on 2021-05-27 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20200730_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hoodie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размер Худи')),
                ('brand_name', models.CharField(max_length=255, verbose_name='Брендовое имя Худи')),
                ('sex', models.CharField(max_length=255, verbose_name='Пол')),
                ('season', models.CharField(max_length=255, verbose_name='Худи для Сезона')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размер кроссовок')),
                ('brand_name', models.CharField(max_length=255, verbose_name='Брендовое имя кроссовок')),
                ('sex', models.CharField(max_length=255, verbose_name='Пол')),
                ('season', models.CharField(max_length=255, verbose_name='Кроссовок для Сезона')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TShirts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размер Футболок')),
                ('brand_name', models.CharField(max_length=255, verbose_name='Брендовое имя Футболок')),
                ('sex', models.CharField(max_length=255, verbose_name='Пол')),
                ('season', models.CharField(max_length=255, verbose_name='Футболки для Сезона')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
