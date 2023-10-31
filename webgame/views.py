from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

from engine.GameStart import GameStart
from engine.Query import Query
from engine.TakeDifferentColorToken import TakeDifferentColorToken
from repository.GameRepositoryInMemory import GameRepositoryInMemory
from webgame.forms import TokenForm


# Create your views here.
def index(request):
    return HttpResponse("Hello world")


def game_launcher(request):
    game_repository = GameRepositoryInMemory()
    GameStart(game_repository).execute(number_of_player=2)
    return HttpResponse(str(game_repository.get_game()))


def take_different_tokens(request, player_number):
    # game launch
    game_repository = GameRepositoryInMemory()
    game_start = GameStart(game_repository)
    query = Query(game_repository)
    game_start.execute(2)
    game_state = query.show_game_state()

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TokenForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TokenForm()

        for color in game_state.board.stock.__dict__:
            if game_state.board.stock.__dict__[color] <= 0:
                form.fields.pop(color)

        form.fields.pop('red')

    return render(request, "webgame/take_different_tokens.html", {"tokenform": form})

