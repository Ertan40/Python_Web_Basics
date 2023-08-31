from django.db import models
from enum import Enum
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils import timezone

# Create your models here.


def validate_date(value):
    if value < timezone.now().date():
        raise ValidationError("The date cannot be in the past!")


def validate_first_name(value):
    if not value.isalpha():
        raise ValidationError("The name should contain only letters!")


def validate_password(value):
    if not any(char.isdigit() for char in value):
        raise ValidationError("The password must contain at least 1 digit.")


class Profile(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=20, validators=(validate_first_name,))
    last_name = models.CharField(null=False, blank=False, max_length=30, validators=[MinLengthValidator(4)])
    email = models.EmailField(max_length=45, null=False, blank=False)
    profile_picture = models.URLField(null=True, blank=True)
    password = models.CharField(max_length=20, null=False, blank=False, validators=[MinLengthValidator(5), validate_password])


# "Sports", "Festivals", "Conferences", "Performing Art", "Concerts", "Theme Party" and "Other"
class EventTypes(Enum):
    SPORTS = "Sports"
    FESTIVALS = "Festivals"
    CONFERENCES = "Conferences"
    PERFORMING_ART = "Performing Art"
    CONCERTS = "Concerts"
    THEME_PARTY = "Theme Party"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Event(models.Model):
    event_name = models.CharField(max_length=30, validators=[MinLengthValidator(2)], null=False, blank=False, verbose_name='NAME')
    category = models.CharField(null=False, blank=False, choices=EventTypes.choices())
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=False, blank=False, validators=[validate_date])
    event_image = models.URLField(null=False, blank=False)