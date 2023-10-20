from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date', 'is_published')
    search_fields = ('name',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'

