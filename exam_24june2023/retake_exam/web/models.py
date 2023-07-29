from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_names_start_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validate_fruit_name(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError("Fruit name should contain only letters!")


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=25, validators=[MinLengthValidator(2), validate_names_start_with_letter],
                                  null=False, blank=False)
    last_name = models.CharField(max_length=35, validators=[MinLengthValidator(1), validate_names_start_with_letter],
                                  null=False, blank=False)
    email = models.EmailField(max_length=40, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False, validators=(MinLengthValidator(8),))
    image_url = models.URLField(null=True, blank=True)
    age = models.URLField(null=True, blank=True, default=18)


class Fruit(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(2,), validate_fruit_name],
                            null=False, blank=False)
    image_url = models.URLField(null=True, blank=True, verbose_name='Image URL')
    description = models.TextField(null=False, blank=False)
    nutrition = models.TextField(null=True, blank=True)