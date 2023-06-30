from django.contrib import admin

from gamesplay_app.gamesplay.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...