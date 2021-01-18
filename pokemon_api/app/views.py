from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Hello Pokemon API")


def pokemons(request):
    if request.method == 'GET':
        return HttpResponse('Request sent with GET method')

    if request.method == 'POST':
        pass
    
