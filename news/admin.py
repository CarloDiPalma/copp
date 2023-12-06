from django import forms
from django.contrib import admin
from django.contrib.admin import TabularInline
from ckeditor.widgets import CKEditorWidget

from .models import Post, PostImage


class PostImageInline(TabularInline):
    model = PostImage
    extra = 1


class PostAdminForm(forms.ModelForm):
    short_story = forms.CharField(widget=CKEditorWidget())
    full_story = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('pk', 'h1', 'is_published', 'date')
    search_fields = ('h1',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'
    inlines = (PostImageInline,)


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post', 'image')
    search_fields = ('post',)
    empty_value_display = '-пусто-'


