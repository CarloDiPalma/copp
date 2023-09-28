from django.contrib import admin

from .models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'edu_start', 'is_free')
    # list_editable = ('is_free',)
    search_fields = ('name',)
    list_filter = ('edu_start',)
    empty_value_display = '-пусто-'
