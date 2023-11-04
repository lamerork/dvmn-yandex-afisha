from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    description_short = models.TextField('Кратое описание', blank=True)
    description_long = HTMLField('Описание', blank=True)
    lng = models.FloatField('Координаты долготы')
    lat = models.FloatField('Координаты широты')

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    image = models.ImageField('Изображение')
    position = models.IntegerField('Позиция', default=0)
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE, verbose_name='Место')

    class Meta:
         ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place.title}'
