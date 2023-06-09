# Generated by Django 4.2.1 on 2023-05-31 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_department_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code_name', models.CharField(max_length=15, unique=True)),
                ('dead_line', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(to='web.project'),
        ),
    ]
