from django.db import models


class MyDb(models.Model):
    store_name = models.CharField(max_length=50, verbose_name="Название магазина")
    link = models.TextField(null=True, blank=True, verbose_name="Ссылка")
    content = models.TextField(null=True, blank=True, verbose_name="Описание акции")
    code = models.CharField(max_length=100, blank=True, verbose_name="Промокод")
    discount = models.CharField(max_length=30, verbose_name="Скидка")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    discount_start = models.DateField(db_index=True, verbose_name="Начало действия скидки")
    discount_end = models.DateField(db_index=True, verbose_name="Конец действия скидки")
    rubric = models.ForeignKey('Rubrics', on_delete=models.PROTECT, null=True, verbose_name="Рубрика")

    class Meta:
        verbose_name_plural = "Скидки"
        verbose_name = "Скидка"
        ordering = ["-discount"]


class Rubrics(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ["name"]
