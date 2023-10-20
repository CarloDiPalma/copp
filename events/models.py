from django.db import models


class Event(models.Model):
    """Мероприятие."""

    name = models.CharField(
        max_length=140,
        verbose_name='Имя мероприятия'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание мероприятия',
        help_text='Описание мероприятия'
    )
    image = models.ImageField(
        upload_to='events/images',
        verbose_name='Изображение'
    )
    date = models.DateTimeField(
        verbose_name='Дата мероприятия',
    )
    duration = models.PositiveSmallIntegerField(
        verbose_name='Длительность мероприятия',
    )
    text = models.TextField(
        verbose_name='Подробное описание программы',
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Мероприятие опубликовано'
    )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.name
