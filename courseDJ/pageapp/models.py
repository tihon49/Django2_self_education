from django.db import models



# Create your models here.
class Page(models.Model):
    '''Модель страницы'''
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    active = models.BooleanField('Вкл/Выкл', default=True)
    template = models.CharField('Template', default='page/index.html', max_length=1000)
    slug = models.SlugField('url', max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'