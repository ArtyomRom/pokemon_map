from django.db import models, migrations  # noqa F401
from django.utils import timezone

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemon_map/pokemon_entities/', blank=True, null=True)

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=timezone.now)
    disappeared_at = models.DateTimeField(default=timezone.now)
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.pokemon} ({self.lat}, {self.lon})'

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
