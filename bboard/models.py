from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError


class MyDb(models.Model):
    """Model for discounts information"""
    store_name = models.CharField(max_length=50, verbose_name="Название магазина")
    link = models.TextField(null=True, blank=True, verbose_name="Ссылка",
                            validators=[validators.URLValidator()],
                            error_messages={'invalid': 'Некорректно задана ссылка'})
    content = models.TextField(null=True, blank=True, verbose_name="Описание акции")
    code = models.CharField(max_length=100, blank=True, verbose_name="Промокод")
    discount = models.CharField(max_length=30, verbose_name="Скидка",
                                validators=[validators.RegexValidator(regex='^[1-9][0-9]%$')],
                                error_messages={'invalid': 'Скидка может быть от 1 до 99 процентов'})
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    discount_start = models.DateField(db_index=True, verbose_name="Начало действия скидки")
    discount_end = models.DateField(db_index=True, verbose_name="Конец действия скидки")
    rubric = models.ForeignKey(
        'Rubrics',
        on_delete=models.PROTECT,
        null=True,
        verbose_name="Рубрика",
        related_name="discounts"
    )

    def clean(self):
        """This function validates field 'Content' of MyDb model (it shouldn't be empty)"""
        errors = {}
        if not self.content:
            errors['content'] = ValidationError('Укажите описание скидки')

        if errors:
            raise ValidationError(errors)

    class Meta:
        """Meta-information of MyDb model"""
        verbose_name_plural = "Скидки"
        verbose_name = "Скидка"
        ordering = ["-discount"]


class Rubrics(models.Model):
    """Model for rubrics of the discounts"""
    name = models.CharField(max_length=30, db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ["name"]
