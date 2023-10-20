from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'is_active', 'last_name')
    search_fields = ('last_name', 'email')
    # list_filter = ('date',)
    empty_value_display = '-пусто-'
