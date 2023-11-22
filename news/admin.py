from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import Post, PostImage


class PostImageInline(TabularInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'h1', 'is_published', 'date')
    search_fields = ('h1',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'
    inlines = (PostImageInline,)


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post', 'image')
    search_fields = ('post',)
    empty_value_display = '-пусто-'
