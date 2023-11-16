# Generated by Django 4.2.5 on 2023-11-15 09:09

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('edu_progs', '0003_order_name_alter_order_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='handled',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата обработки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Номер телефона', max_length=128, region=None, verbose_name='Номер телефона'),
        ),
    ]