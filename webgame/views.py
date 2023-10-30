from django.http import HttpResponse
from django.shortcuts import render

from engine.GameStart import GameStart
from repository.GameRepositoryInMemory import GameRepositoryInMemory


# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def game_launcher(request):
    game_repository = GameRepositoryInMemory()
    GameStart(game_repository).execute(number_of_player=2)
    return HttpResponse(str(game_repository.get_game()))