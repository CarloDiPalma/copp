# Generated by Django 4.2.5 on 2023-11-16 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu_progs', '0004_alter_order_created_alter_order_handled_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='edu_end',
        ),
        migrations.RemoveField(
            model_name='program',
            name='edu_start',
        ),
        migrations.RemoveField(
            model_name='program',
            name='hours',
        ),
    ]