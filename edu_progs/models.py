from django.db import models


class Program(models.Model):
    """Учебная программа."""

    name = models.CharField(max_length=140)
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание группы',
        help_text='Описание программы'
    )
    image = models.ImageField(
        upload_to='programs/images'
    )
    reg_start = models.DateTimeField(
        verbose_name='дата начала регистрации',
    )
    reg_end = models.DateTimeField(
        verbose_name='дата конца регистрации',
    )
    edu_start = models.DateTimeField(
        verbose_name='дата начала обучения',
    )
    edu_end = models.DateTimeField(
        verbose_name='дата конца обучения',
    )
    is_intramural = models.BooleanField(
        verbose_name='флаг очной формы',
        default=True
    )
    is_free = models.BooleanField()
    text = models.TextField(
        verbose_name='подробное описание программы',
    )

    class Meta:
        verbose_name = 'Учебная программа'
        verbose_name_plural = 'Учебные программы'

    def __str__(self):
        return self.name
