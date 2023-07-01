# Generated by Django 4.2.2 on 2023-06-27 07:00

import django.core.validators
from django.db import migrations, models
import petstagram.core.model_mixins
import petstagram.photos.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/', validators=[petstagram.photos.validators.validate_file_size])),
                ('description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('publication_date', models.DateField(auto_now=True)),
                ('tagged_pets', models.ManyToManyField(blank=True, to='pets.pet')),
            ],
            bases=(petstagram.core.model_mixins.StrFromFieldsMixin, models.Model),
        ),
    ]
