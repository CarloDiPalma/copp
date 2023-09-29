from django.db import models


class Program(models.Model):
    """Учебная программа."""

    name = models.CharField(
        max_length=140,
        verbose_name='Имя программы'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание программы',
        help_text='Описание программы'
    )
    image = models.ImageField(
        upload_to='programs/images',
        verbose_name='Изображение'
    )
    reg_start = models.DateField(
        verbose_name='Дата начала регистрации',
    )
    reg_end = models.DateField(
        verbose_name='Дата конца регистрации',
    )
    edu_start = models.DateField(
        verbose_name='Дата начала обучения',
    )
    edu_end = models.DateField(
        verbose_name='Дата конца обучения',
    )
    hours = models.PositiveSmallIntegerField(
        verbose_name='Трудоёмкость',
    )
    is_intramural = models.BooleanField(
        verbose_name='Очная форма',
        default=True
    )
    is_free = models.BooleanField(
        verbose_name='Бесплатная программа'
    )
    text = models.TextField(
        verbose_name='Подробное описание программы',
    )
    is_published = models.BooleanField(
        verbose_name='Программа опубликована',
    )

    class Meta:
        verbose_name = 'Учебная программа'
        verbose_name_plural = 'Учебные программы'

    def __str__(self):
        return self.name
