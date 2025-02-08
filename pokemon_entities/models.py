from django.db import models, migrations  # noqa F401
from django.utils import timezone


class Pokemon(models.Model):
    '''Покемон'''
    title = models.CharField('Имя', max_length=200, blank=True)
    image = models.ImageField('Картинка', upload_to='pokemon_map/pokemon_entities/', blank=True, null=True,
                              default=None)
    description = models.TextField('Описание', blank=True, default='Информации о покемоне нет')
    title_en = models.CharField('Имя по английски', max_length=200, null=True)
    title_jp = models.CharField('Имя по японски', max_length=200, null=True)
    previous_evolution = models.ForeignKey('self', verbose_name='Предок',
                                           on_delete=models.SET_NULL,
                                           null=True,
                                           related_name='next_evolutions',
                                           blank=True, )
    next_evolution = models.ForeignKey('self', verbose_name='Потомок',
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       related_name='previous_evolution_v2',
                                       blank=True, )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    '''Сущность покемона'''
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.SET_NULL, null=True)
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


class Migration(migrations.Migration):
    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]
    # your models here
    operations = [migrations.CreateModel(
        name='Pokemon',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('title', models.CharField(max_length=255)),
        ]
    )]
