from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'h1', 'is_published', 'date')
    search_fields = ('h1',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'
