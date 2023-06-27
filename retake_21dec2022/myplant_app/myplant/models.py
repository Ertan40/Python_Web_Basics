from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from enum import Enum

# Create your models here.
def validate_first_letter(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')

def validate_plant_name(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")


class Profile(models.Model):
    username = models.CharField(null=False, blank=False, max_length=10, validators=(MinLengthValidator(2),))
    first_name = models.CharField(null=False, blank=False, max_length=20, validators=(validate_first_letter,))
    last_name = models.CharField(null=False, blank=False, max_length=20, validators=(validate_first_letter,))
    profile_picture = models.URLField(null=True, blank=True)


class PlantTypes(Enum):
    OUTDOOR = "Outdoor Plants"
    INDOOR = "Indoor Plants"

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Plant(models.Model):
    plant_type = models.CharField(null=False, blank=False, max_length=14, choices=PlantTypes.choices())
    name = models.CharField(null=False, blank=False, max_length=20, validators=[
                                    validate_plant_name,
                                    MinLengthValidator(2),
                                    ])
    image_url = models.URLField(null=False, blank=False, verbose_name='Image URL')
    description = models.TextField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
