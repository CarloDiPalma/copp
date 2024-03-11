from django import forms
from django.contrib import admin
from django.contrib.admin import TabularInline
from ckeditor.widgets import CKEditorWidget

from vacancy.models import Vacancy


class VacancyAdminForm(forms.ModelForm):
    short_story = forms.CharField(widget=CKEditorWidget())
    full_story = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Vacancy
        fields = '__all__'


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    form = VacancyAdminForm
    list_display = ('pk', 'title', 'is_published', 'date')
    search_fields = ('title',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'
