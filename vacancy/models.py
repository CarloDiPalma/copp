from django.db import models


class Vacancy(models.Model):
    """Вакансия."""
    title = models.CharField(
        max_length=140,
        verbose_name='Заголовок вакансии',
        help_text='Заголовок вакансии'
    )
    short_story = models.TextField(
        verbose_name='Краткая новость',
        help_text='Краткая новость'
    )
    full_story = models.TextField(
        null=True,
        blank=True,
        verbose_name='Полное описание вакансии',
        help_text='Полное описание вакансии'
    )
    date = models.DateTimeField(
        verbose_name='Дата публикации',
        help_text='Дата публикации'
    )
    is_published = models.BooleanField(
        verbose_name='Вакансия опубликована',
    )

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title
