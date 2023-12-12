from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Event


class EventAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Event
        fields = '__all__'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ('pk', 'name', 'date', 'is_published')
    search_fields = ('name',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'

