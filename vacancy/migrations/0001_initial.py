# Generated by Django 4.2.5 on 2024-03-11 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Заголовок вакансии', max_length=140, verbose_name='Заголовок вакансии')),
                ('short_story', models.TextField(help_text='Краткая новость', verbose_name='Краткая новость')),
                ('full_story', models.TextField(blank=True, help_text='Полное описание вакансии', null=True, verbose_name='Полное описание вакансии')),
                ('date', models.DateTimeField(help_text='Дата публикации', verbose_name='Дата публикации')),
                ('is_published', models.BooleanField(verbose_name='Вакансия опубликована')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
