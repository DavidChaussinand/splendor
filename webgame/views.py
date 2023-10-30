from django.http import HttpResponse
from django.template import loader

from engine.GameStart import GameStart
from engine.Query import Query
from engine.TakeDifferentColorToken import TakeDifferentColorToken
from repository.GameRepositoryInMemory import GameRepositoryInMemory


# Create your views here.
def index(request):
    return HttpResponse("Hello world")


def take_different_tokens(request, player_number):
    game_repository = GameRepositoryInMemory()
    game_start = GameStart(game_repository)
    query = Query(game_repository)
    take_different_color_token = TakeDifferentColorToken(game_repository)

    game_start.execute(2)
    game_state = query.show_game_state()
    template = loader.get_template("webgame/take_different_tokens.html")
    context = {}
    return HttpResponse(template.render(context,request))