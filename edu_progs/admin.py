from django.contrib import admin

from .models import Program, Order


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'edu_start', 'is_free')
    # list_editable = ('is_free',)
    search_fields = ('name',)
    list_filter = ('edu_start',)
    empty_value_display = '-пусто-'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'phone', 'email', 'created', 'program', 'is_handled')
    readonly_fields = ['created', 'phone', 'email', 'name', 'program']
    search_fields = ('email',)
    list_filter = ('created',)
