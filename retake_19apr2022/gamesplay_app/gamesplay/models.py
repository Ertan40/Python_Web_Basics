from enum import Enum
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class Profile(models.Model):
    email = models.EmailField(null=False, blank=False)
    age = models.IntegerField(null=False, blank=False, validators=(MinValueValidator(12),))
    password = models.CharField(null=False, blank=False, max_length=30)
    first_name = models.CharField(null=True, blank=True, max_length=30)
    last_name = models.CharField(null=True, blank=True, max_length=30)
    profile_picture = models.URLField(null=True, blank=True)

# "Action", "Adventure", "Puzzle", "Strategy", "Sports", "Board/Card Game", and "Other".

class GameCategories(Enum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Game(models.Model):
    title = models.CharField(null=False, blank=False, max_length=30, unique=True)
    category = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        choices=GameCategories.choices())
    rating = models.FloatField(null=False, blank=False,
                            validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    max_level = models.IntegerField(null=True, blank=True, validators=(MinValueValidator(1),))
    image_url = models.URLField(null=False, blank=False, verbose_name='Image URL')
    summary = models.TextField(null=True, blank=True)