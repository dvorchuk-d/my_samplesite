# Generated by Django 3.2.8 on 2022-01-08 18:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20211018_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydb',
            name='discount',
            field=models.CharField(error_messages={'invalid': 'Скидка может быть от 1 до 99 процентов'}, max_length=30, validators=[django.core.validators.RegexValidator(regex='^[1-9][0-9]%$')], verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='mydb',
            name='link',
            field=models.TextField(blank=True, error_messages={'invalid': 'Некорректно задана ссылка'}, null=True, validators=[django.core.validators.URLValidator()], verbose_name='Ссылка'),
        ),
    ]