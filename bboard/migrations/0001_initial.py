# Generated by Django 3.2.8 on 2022-01-10 16:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MyDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50, verbose_name='Название магазина')),
                ('link', models.TextField(blank=True, error_messages={'invalid': 'Некорректно задана ссылка'}, null=True, validators=[django.core.validators.URLValidator()], verbose_name='Ссылка')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание акции')),
                ('code', models.CharField(blank=True, max_length=100, verbose_name='Промокод')),
                ('discount', models.CharField(error_messages={'invalid': 'Скидка может быть от 1 до 99 процентов'}, max_length=30, validators=[django.core.validators.RegexValidator(regex='^[1-9][0-9]%$')], verbose_name='Скидка')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('discount_start', models.DateField(db_index=True, verbose_name='Начало действия скидки')),
                ('discount_end', models.DateField(db_index=True, verbose_name='Конец действия скидки')),
                ('rubric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.rubrics', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
                'ordering': ['-discount'],
            },
        ),
    ]
