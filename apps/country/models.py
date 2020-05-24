from django.db import models

from apps.core.api.models import DateFields


class Country(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=255
    )
    code = models.CharField(
        verbose_name='Код страны',
        max_length=12,
        blank=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class CountryStatistic(models.Model):
    country = models.ForeignKey(
        Country,
        verbose_name='Страна',
        related_name='statistic',
        on_delete=models.CASCADE
    )
    confirmed = models.PositiveIntegerField(
        verbose_name='Общее количество случаев заражения',
        null=True,
        blank=True

    )
    deaths = models.PositiveIntegerField(
        verbose_name='Общее количество смертей',
        null=True,
        blank=True
    )
    province = models.CharField(
        verbose_name='Провинция',
        max_length=255,
        default='',
        blank=True
    )
    recovered = models.PositiveIntegerField(
        verbose_name='Общее количество выздоровевших',
        null=True,
        blank=True
    )
    last_updated = models.DateTimeField(
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Статистика страны'
        verbose_name_plural = 'Статистики стран'

    def __str__(self):
        return self.country.name

