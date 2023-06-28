from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from enum import Enum
# Create your models here.


def validate_username(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

class Profile(models.Model):
    username = models.CharField(max_length=15, null=False, blank=False,
                                validators=[MinLengthValidator(2), validate_username])
    email = models.EmailField(null=False, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)


class AlbumGenres(Enum):
    # "Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music",
    # "Dance Music", "Hip Hop Music", and "Other".
    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP__MUSIC = "Hip Hop Music"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

class Album(models.Model):
    album_name = models.CharField(null=False, blank=False, max_length=30, unique=True)
    artist = models.CharField(null=False, blank=False, max_length=30)
    genre = models.CharField(null=False, blank=False, max_length=30, choices=AlbumGenres.choices())
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=False, blank=False, verbose_name='Image URL')
    price = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0)])

    class Meta:
        ordering = ('pk',)