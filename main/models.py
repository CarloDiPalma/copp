from django.db import models


class SingletonModel(models.Model):
    """Abstract Singleton Django Model"""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class People(SingletonModel):
    count = models.PositiveIntegerField(
        default=0,
        verbose_name='Число охваченных людей',
        help_text='Число охваченных людей'
    )

    def __str__(self):
        return str(f'Объект синглтон с айди {self.pk}')
