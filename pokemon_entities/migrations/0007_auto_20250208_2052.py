# Generated by Django 3.1.14 on 2025-02-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20250206_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='text',
            field=models.TextField(blank=True, default='Информации о покемоне нет', null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='pokemon_map/pokemon_entities/'),
        ),
    ]
