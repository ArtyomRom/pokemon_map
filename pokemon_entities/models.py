from django.db import models, migrations  # noqa F401
from django.core.validators import MinValueValidator

class Pokemon(models.Model):
    '''Покемон'''
    title = models.CharField('Имя покемона', max_length=200, blank=False, null=False)
    image = models.ImageField('Изображения покемона', upload_to='pokemon_map/pokemon_entities/', blank=True, null=True,
                              default=None)
    description = models.TextField('Описание покемона', blank=True, default='Информации о покемоне нет')
    title_en = models.CharField('Имя по английски', max_length=200, null=False)
    title_jp = models.CharField('Имя по японски', max_length=200, null=False)
    previous_evolution = models.ForeignKey('self', verbose_name='Предок',
                                           on_delete=models.SET_NULL,
                                           null=True,
                                           related_name='next_evolutions',
                                           blank=True, )


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    '''Сущность покемона'''
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.PROTECT, null=False, blank=False, related_name='pokemon_entity')
    lat = models.FloatField('Долгота')
    lon = models.FloatField('Широта')
    appeared_at = models.DateTimeField('Появился на карте')
    disappeared_at = models.DateTimeField('Исчез с карты')
    level = models.IntegerField('Уровень', default=0, blank=False, null=False, validators=[MinValueValidator(0)])
    health = models.IntegerField('Здоровье', default=0, blank=False, null=False, validators=[MinValueValidator(0)])
    strength = models.IntegerField('Сила', default=0, blank=False, null=False, validators=[MinValueValidator(0)])
    defence = models.IntegerField('Защита', default=0, blank=False, null=False, validators=[MinValueValidator(0)])
    stamina = models.IntegerField('Выносливость', default=0, blank=False, null=False, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.pokemon}, {self.lat}, {self.lon}'


