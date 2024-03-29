# Generated by Django 4.2.5 on 2024-03-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('user', 'Пользователь'), ('organization', 'Организация'), ('admin', 'Администратор'), ('teacher', 'Преподаватель'), ('student', 'Обучающийся')], default='user', max_length=20),
        ),
    ]
