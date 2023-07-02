# Generated by Django 4.2.2 on 2023-06-21 07:50

import django.core.validators
from django.db import migrations, models
import mymusic_app.mymusic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('POP_MUSIC', 'Pop Music'), ('JAZZ_MUSIC', 'Jazz Music'), ('RNB_MUSIC', 'R&B Music'), ('ROCK_MUSIC', 'Rock Music'), ('COUNTRY_MUSIC', 'Country Music'), ('DANCE_MUSIC', 'Dance Music'), ('HIP_HOP__MUSIC', 'Hip Hop Music'), ('OTHER', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), mymusic_app.mymusic.models.validate_username])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]