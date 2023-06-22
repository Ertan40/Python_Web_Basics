from django.contrib import admin

from notes_app.notes.models import Profile, Note


# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    ...


@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    ...