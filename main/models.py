from django.db import models


class People(models.Model):
    count = models.PositiveIntegerField(
        default=0,
        verbose_name='Число охваченных людей',
        help_text='Число охваченных людей'
    )
