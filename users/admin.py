from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    ordering = ('email', )


@admin.register(User)
class UserAdmin(CustomUserAdmin):
    list_display = ('pk', 'email', 'is_active', 'last_name')
    search_fields = ('last_name', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    # list_filter = ('date',)
    empty_value_display = '-пусто-'
