from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_employee_photo_alter_employee_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ("Id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=15)),
            ],
        ),
    ]