from django.db import models, migrations  # noqa F401
from django.utils import timezone


class Pokemon(models.Model):
    '''Покемон'''
    title = models.CharField('Имя', max_length=200, blank=False, null=False)
    image = models.ImageField('Картинка', upload_to='pokemon_map/pokemon_entities/', blank=True, null=True,
                              default=None)
    description = models.TextField('Описание', blank=True, default='Информации о покемоне нет')
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
    lat = models.FloatField('Долгота', blank=True)
    lon = models.FloatField('Широта', blank=True)
    appeared_at = models.DateTimeField('Появился', default=timezone.now, blank=True)
    disappeared_at = models.DateTimeField('Исчез', default=timezone.now, blank=True)
    level = models.IntegerField('Уровень', default=0)
    health = models.IntegerField('Здоровье', default=0)
    strength = models.IntegerField('Сила', default=0)
    defence = models.IntegerField('Защита', default=0)
    stamina = models.IntegerField('Выносливость', default=0)

    def __str__(self):
        return f'{self.pokemon}, {self.lat}, {self.lon}'


