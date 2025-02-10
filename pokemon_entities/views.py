import folium
from django.shortcuts import render
from django.utils import timezone

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    # with open('pokemon_entities/pokemons.json', encoding='utf-8') as database:
    #     pokemons = json.load(database)['pokemons']

    today = timezone.now()
    pokemons_entity = PokemonEntity.objects.filter(disappeared_at__lte=today, appeared_at__lte=today)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entity:
        # for pokemon_entity in pokemon['entities']:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon_entity.pokemon.image.path if pokemon_entity.pokemon.image else DEFAULT_IMAGE_URL
        )
    pokemons = Pokemon.objects.all()

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url if pokemon.image else '',
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    # with open('pokemon_entities/pokemons.json', encoding='utf-8') as database:
    #     pokemons = json.load(database)['pokemons']
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemons = PokemonEntity.objects.filter(pokemon=pokemon)
    evolution = pokemon.next_evolutions.all()[0] if pokemon.next_evolutions.all() else ''
    # for pokemon in pokemons:
    #     if pokemon['pokemon_id'] == int(pokemon_id):
    #         requested_pokemon = pokemon
    #         break
    # else:
    #     return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon_entity.pokemon.image.path if pokemon_entity.pokemon.image else DEFAULT_IMAGE_URL
        )

    # pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon_entity = {
        'pokemon_id': pokemon.id,
        'img_url': pokemon.image.url if pokemon.image else '',
        'title_ru': pokemon.title,
        'description': pokemon.description,
        'title_jp': pokemon.title_jp,
        'title_en': pokemon.title_en,
        'previous_evolution': {
            'id': pokemon.previous_evolution.id,
            'img_url': pokemon.previous_evolution.image.url if pokemon.previous_evolution and pokemon.previous_evolution.image else '',
            'title_ru': pokemon.previous_evolution.title if pokemon.previous_evolution else '',
        } if pokemon.previous_evolution else None,
        'next_evolution': {
            'id': evolution.id,
            'img_url': evolution.image.url if evolution.image else '',
            'title_ru': evolution.title if evolution.title else '',
        } if evolution else None,

    }
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_entity
    })

# if __name__ == '__main__':
#     show_all_pokemons()
