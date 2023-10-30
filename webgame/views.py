from django.http import HttpResponse
from django.shortcuts import render

from engine.GameStart import GameStart
from engine.Query import Query
from repository.GameRepositoryInMemory import GameRepositoryInMemory


# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def game_launcher(request, numberofplayer):
    game_repository = GameRepositoryInMemory()
    GameStart(game_repository).execute(number_of_player=numberofplayer)
    query = Query(game_repository).show_game_state()
    return HttpResponse(str(query))

