from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    """Новостной пост."""
    h1 = models.CharField(
        max_length=140,
        verbose_name='Заголовок поста',
        help_text='Заголовок поста'
    )
    description = models.CharField(
        max_length=160,
        null=True,
        blank=True,
        verbose_name='Метатег description',
        help_text='Метатег description'
    )
    title = models.CharField(
        max_length=65,
        null=True,
        blank=True,
        verbose_name='Метатег title',
        help_text='Метатег title'
    )
    short_story = models.TextField(
        verbose_name='Краткая новость',
        help_text='Краткая новость'
    )
    full_story = models.TextField(
        null=True,
        blank=True,
        verbose_name='Полная новость',
        help_text='Полная новость'
    )
    image = models.ImageField(
        upload_to='news/images',
        verbose_name='Изображение',
        null=True
    )
    date = models.DateTimeField(
        verbose_name='Дата публикации',
        help_text='Дата публикации'
    )
    is_published = models.BooleanField(
        verbose_name='Пост опубликован',
    )

    class Meta:
        verbose_name = 'Новостной пост'
        verbose_name_plural = 'Новостные посты'

    def __str__(self):
        return self.h1


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "news/images/%s-%s" % (slug, filename)


class PostImage(models.Model):
    """Изображение в новостном посте."""
    post = models.ForeignKey(
        Post,
        default=None,
        on_delete=models.CASCADE,
        verbose_name='Пост, в котором будет изображение'
    )
    image = models.ImageField(
        upload_to='news/images',
        verbose_name='Image'
    )

    class Meta:
        verbose_name = 'Изображение в посте'
        verbose_name_plural = 'Изображения в постах'
