# Generated by Django 3.1.14 on 2025-02-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20250204_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='pokemon_map/pokemon_entities/'),
        ),
    ]
