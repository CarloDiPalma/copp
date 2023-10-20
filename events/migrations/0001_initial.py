# Generated by Django 4.2.5 on 2023-10-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='Имя мероприятия')),
                ('description', models.TextField(blank=True, help_text='Описание мероприятия', null=True, verbose_name='Описание мероприятия')),
                ('image', models.ImageField(upload_to='events/images', verbose_name='Изображение')),
                ('date', models.DateTimeField(verbose_name='Дата мероприятия')),
                ('duration', models.PositiveSmallIntegerField(verbose_name='Длительность мероприятия')),
                ('text', models.TextField(verbose_name='Подробное описание программы')),
                ('is_published', models.BooleanField(default=False, verbose_name='Мероприятие опубликовано')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]