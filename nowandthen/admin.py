from django.contrib import admin

# Register your models here.
from nowandthen.models import Picture
from nowandthen.models import Comment
from nowandthen.models import UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('picture', )


class PictureAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'description', 'tag_one', 'tag_two', 'era',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('image', 'user', 'body', 'created_on')
    list_filter = ('image', 'created_on')


admin.site.register(Picture, PictureAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile)
