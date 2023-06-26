from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    image_url = models.URLField(null=False, blank=False, verbose_name='Image URL')


class Book(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(null=False, blank=False, verbose_name='Image URL')
    type = models.CharField(max_length=30, null=False, blank=False)