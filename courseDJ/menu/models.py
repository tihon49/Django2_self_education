from django.db import models

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(models.Model):
    '''Модель меню'''
    name = models.CharField('Имя', max_length=100)
    is_auth = models.BooleanField('Для зарегистрированных?', default=True)
    active = models.BooleanField('Вкл/Выкл', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'



class MenuItems(MPTTModel):
    '''Модель пунктов меню'''
    name = models.CharField('Название на литинице', max_length=100)
    title = models.CharField('Название на русском', max_length=100)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    status = models.BooleanField('Вкл/Выкл', default=True)
    is_auth = models.BooleanField('Для зарегистрированных?', default=True)
    anchor = models.CharField('Якорь', max_length=30)
    url = models.URLField('Ссылка на внешний ресурс', max_length=1000)
    active = models.BooleanField('Вкл/Выкл', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'