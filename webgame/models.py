from django.db import models


# Create your models here.


class Stock(models.Model):
    red = models.IntegerField(default=0)
    # green = models.IntegerField(default=0)
    # blue = models.IntegerField(default=0)
    # black = models.IntegerField(default=0)
    # white = models.IntegerField(default=0)


class Board(models.Model):
    # yellow = models.IntegerField(default=5)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    # noble_number = models.IntegerField(default=0)
    # card_level1 = models.IntegerField(default=0)
    # card_level2 = models.IntegerField(default=0)
    # card_level3 = models.IntegerField(default=0)
    # cards = models.JSONField


class Game(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)


class Player(models.Model):
    # yellow = models.IntegerField(default=0)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    # noble_number = models.IntegerField(default=0)
    # cards = models.JSONField
    # cards_reserved = models.JSONField
