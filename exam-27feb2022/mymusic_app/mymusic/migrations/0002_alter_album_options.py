# Generated by Django 4.2.2 on 2023-06-21 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('pk',)},
        ),
    ]