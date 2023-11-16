from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


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
        default=False,
        verbose_name='Программа опубликована'
    )

    class Meta:
        verbose_name = 'Учебная программа'
        verbose_name_plural = 'Учебные программы'

    def __str__(self):
        return self.name


class Order(models.Model):
    """Заявка на программу."""
    name = models.CharField(
        max_length=100,
        verbose_name="Имя заявителя",
        null=True
    )
    program = models.ForeignKey(
        Program,
        verbose_name="Программа в заявке",
        on_delete=models.CASCADE
    )
    phone = PhoneNumberField(
        verbose_name="Номер телефона",
        help_text="Номер телефона",
        null=False,
        blank=False
    )
    email = models.EmailField(
        verbose_name="Почта",
        max_length=254
    )
    created = models.DateTimeField(
        verbose_name='Дата заявки',
        auto_now_add=True
    )
    handled = models.DateTimeField(
        verbose_name='Дата обработки',
        null=True,
        blank=True
    )
    is_handled = models.BooleanField(
        verbose_name='Заявка обработана',
        default=False
    )
    note = models.TextField(
        verbose_name='Заметка для менеджера',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Заявка на программу'
        verbose_name_plural = 'Заявки на программы'

    def __str__(self):
        return f'{self.name} {str(self.phone)} {self.email}'

