# Generated by Django 3.1.14 on 2025-02-10 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20250210_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pokemon_entity', to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]
