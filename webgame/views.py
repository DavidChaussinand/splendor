from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect

from engine.GameStart import GameStart
from engine.Query import Query
from engine.TakeDifferentColorToken import TakeDifferentColorToken
from repository.GameRepositoryInMemory import GameRepositoryInMemory
from webgame.forms import TokenForm

game_repository = GameRepositoryInMemory()


# Create your views here.
def index(request):
    return render(request, "webgame/index.html")


def game_launcher(request):
    GameStart(game_repository).execute(number_of_player=2)
    return redirect("board")

def board(request):

    game_state = game_repository.get_game()
    return render(request, "webgame/board.html", {"game_state": game_state})


def take_different_tokens(request, player_number):
    query = Query(game_repository)
    game_state = query.show_game_state()

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TokenForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            take_different_token = TakeDifferentColorToken(game_repository)
            take_different_token.execute(0, blue=form.cleaned_data["blue"], black=form.cleaned_data["black"], white=form.cleaned_data["white"], red= form.cleaned_data["red"], green=form.cleaned_data["green"])
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect("board")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TokenForm()

        for color in game_state.board.stock.__dict__:
            if game_state.board.stock.__dict__[color] <= 0:
                form.fields.pop(color)

    return render(request, "webgame/take_different_tokens.html", {"tokenform": form})

