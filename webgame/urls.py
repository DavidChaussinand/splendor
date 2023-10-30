from django.urls import path

from webgame import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gamelauncher/<int:numberofplayer>/", views.game_launcher, name="launchgame"),

]