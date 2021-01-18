from django.shortcuts import HttpResponse
import json
from .models import *

def index(request):
    return HttpResponse("Hello Pokemon API")


def pokemons(request):
    if request.method == 'GET':
        return HttpResponse('Request sent with GET method')

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pokemon = Pokemon.objects.create(
                name=data['name'],
                pokemon_type=data['pokemon_type'],
                ability=data['ability'],
            )
            return HttpResponse(f"Added pokemon {data['name']} with ID {pokemon.id}")
        except:
            return HttpResponse('There was an error while adding the pokemon to the database')
