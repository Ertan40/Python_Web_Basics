# Generated by Django 4.2.1 on 2023-06-04 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):


    dependencies = [
        ('pets', '0004_alter_pet_slug'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('publication_date', models.DateField(auto_now=True)),
                ('tagged_pets', models.ManyToManyField(blank=True, null=True, to='pets.pet')),
            ],
        ),
    ]
