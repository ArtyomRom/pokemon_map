from django.db import models, migrations  # noqa F401
from django.core.validators import MinValueValidator

class Pokemon(models.Model):
    '''Покемон'''
    title = models.CharField(verbose_name='Имя покемона', max_length=200, blank=False, null=False)
    image = models.ImageField(verbose_name='Изображения покемона', upload_to='pokemon_map/pokemon_entities/', blank=True, null=True,
                              default=None)
    description = models.TextField(verbose_name='Описание покемона', blank=True, null=False, default='Информации о покемоне нет')
    title_en = models.CharField(verbose_name='Имя по английски', max_length=200, blank=True, null=False)
    title_jp = models.CharField(verbose_name='Имя по японски', max_length=200, blank=True, null=False)
    previous_evolution = models.ForeignKey('self', verbose_name='Предок',
                                           on_delete=models.SET_NULL,
                                           null=True,
                                           related_name='next_evolutions',
                                           blank=True, )


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    '''Сущность покемона'''
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.PROTECT, null=False, blank=False, related_name='entities')
    lat = models.FloatField(verbose_name='Долгота', null=True, blank=True)
    lon = models.FloatField(verbose_name='Широта', null=True, blank=True)
    appeared_at = models.DateTimeField(verbose_name='Появился на карте', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Исчез с карты', null=True, blank=True)
    level = models.PositiveIntegerField(verbose_name='Уровень', default=0, blank=True, validators=[MinValueValidator(0)])
    health = models.PositiveIntegerField(verbose_name='Здоровье', default=0, blank=True, validators=[MinValueValidator(0)])
    strength = models.SmallIntegerField(verbose_name='Сила', default=0, blank=True, validators=[MinValueValidator(0)])
    defence = models.SmallIntegerField(verbose_name='Защита', default=0, blank=True, validators=[MinValueValidator(0)])
    stamina = models.SmallIntegerField(verbose_name='Выносливость', default=0, blank=True, validators=[MinValueValidator(0)])



    def __str__(self):
        return f'{self.pokemon}, {self.lat}, {self.lon}'


