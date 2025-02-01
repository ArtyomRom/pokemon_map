from django.db import models, migrations  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemon_map/pokemon_entities/', blank=True, null=True)

    def __str__(self):
        return self.title


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
