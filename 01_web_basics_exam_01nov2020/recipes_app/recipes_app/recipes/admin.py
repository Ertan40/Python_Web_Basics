from django.contrib import admin

from recipes_app.recipes.models import Recipe


# Register your models here.
@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    ...