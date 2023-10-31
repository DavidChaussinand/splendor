from django.urls import path

from webgame import views

urlpatterns = [
    path("", views.index, name="index"),
    path("board", views.board, name="board"),
    path("take_different_tokens/<int:player_number>", views.take_different_tokens, name="take_different_tokens"),
    path("gamelauncher", views.game_launcher, name="launchgame")
]