from django.contrib import admin

from .models import Programm


@admin.register(Programm)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'is_free')
    list_editable = ('is_free',)
    search_fields = ('name',)
    list_filter = ('edu_start',)
    empty_value_display = '-пусто-'
