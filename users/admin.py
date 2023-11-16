from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    ordering = ('email', )


@admin.register(User)
class UserAdmin(CustomUserAdmin):
    list_display = ('pk', 'email', 'is_active', 'last_name')
    search_fields = ('last_name', 'email')
    # list_filter = ('date',)
    empty_value_display = '-пусто-'
