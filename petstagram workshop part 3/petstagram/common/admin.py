from django.contrib import admin

from petstagram.common.models import PhotoComment, PhotoLike


# Register your models here.
@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    ...

@admin.register(PhotoLike)
class LikeAdmin(admin.ModelAdmin):
    ...
