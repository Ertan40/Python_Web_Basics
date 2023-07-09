from enum import Enum

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.
def validate_min_user(value):
    if len(value) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")


def validate_car_year(value):
    if value < 1980 or value > 2049:
        raise ValidationError("Year must be between 1980 and 2049")


class Profile(models.Model):
    username = models.CharField(max_length=10, null=False, blank=False,
                                validators=(validate_min_user,))
    # username = models.CharField(max_length=10, null=False, blank=False,
    #                             validators=(MinLengthValidator(2),))
    email = models.EmailField(null=False, blank=False)
    age = models.IntegerField(null=False, blank=False, validators=(MinValueValidator(18),))
    password = models.CharField(max_length=30, null=False, blank=False)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    picture = models.URLField(null=True, blank=True, verbose_name='Profile Picture')

class CarTypes(Enum):
    # "Sports Car", "Pickup", "Crossover", "Minibus" and "Other"
    SPORTS = "Sports Car"
    PICK_UP = "Pickup"
    CROSS = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Car(models.Model):
    type = models.CharField(max_length=10, null=False, blank=False, choices=CarTypes.choices())
    model = models.CharField(max_length=20, null=False, blank=False, validators=(MinLengthValidator(2),))
    year = models.IntegerField(null=False, blank=False, validators=(validate_car_year,))
    image_url = models.URLField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, validators=(MinValueValidator(1),))