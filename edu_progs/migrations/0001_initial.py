# Generated by Django 4.2.5 on 2023-10-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='Имя программы')),
                ('description', models.TextField(blank=True, help_text='Описание программы', null=True, verbose_name='Описание программы')),
                ('image', models.ImageField(upload_to='programs/images', verbose_name='Изображение')),
                ('reg_start', models.DateField(verbose_name='Дата начала регистрации')),
                ('reg_end', models.DateField(verbose_name='Дата конца регистрации')),
                ('edu_start', models.DateField(verbose_name='Дата начала обучения')),
                ('edu_end', models.DateField(verbose_name='Дата конца обучения')),
                ('hours', models.PositiveSmallIntegerField(default=0, verbose_name='Трудоёмкость')),
                ('is_intramural', models.BooleanField(default=True, verbose_name='Очная форма')),
                ('is_free', models.BooleanField(verbose_name='Бесплатная программа')),
                ('text', models.TextField(verbose_name='Подробное описание программы')),
                ('is_published', models.BooleanField(default=False, verbose_name='Программа опубликована')),
            ],
            options={
                'verbose_name': 'Учебная программа',
                'verbose_name_plural': 'Учебные программы',
            },
        ),
    ]
