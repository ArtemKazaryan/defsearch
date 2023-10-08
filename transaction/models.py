from django.db import models
from django.contrib.auth.models import User


class ProfitableTransaction(models.Model):
    date = models.DateField(blank=False, verbose_name='Дата дохода')
    incometype = models.ManyToManyField('IncomeType', blank=True, verbose_name='Тип дохода')
    name = models.CharField(blank=True, max_length=200, verbose_name='Наименование дохода')
    description = models.TextField(null=True, blank=True, verbose_name='Описание дохода')
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Сумма')

    def __str__(self):
        return self.name



class ExpenditureTransaction(models.Model):
    date = models.DateField(blank=False, verbose_name='Дата расхода')
    category = models.ManyToManyField('Category', blank=True, verbose_name='Категория расхода')
    name = models.CharField(blank=True, max_length=200, verbose_name='Наименование расхода')
    description = models.TextField(null=True, blank=True, verbose_name='Описание расхода')
    meter = models.ManyToManyField('Meter', blank=True, verbose_name='Единица измерения товара/услуги')
    quantity = models.DecimalField(null=True, max_digits=20, decimal_places=2, verbose_name='Количество измерителя')
    price = models.DecimalField(null=True, max_digits=20, decimal_places=2, verbose_name='Цена за единицу измерения')

    @property
    def total_cost(self):
        return round(self.quantity * self.price, 2)

    @property
    def metername(self):
        return self.meter

    @property
    def categoryname(self):
        return self.category

    def __str__(self):
        return self.name



class IncomeType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Meter(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
