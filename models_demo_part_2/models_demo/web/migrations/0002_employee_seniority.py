# Generated by Django 4.2.1 on 2023-05-31 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='seniority',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Regular', 'Regular'), ('Senior', 'Senior')], default='Junior', max_length=7, verbose_name='Seniority level'),
        ),
    ]