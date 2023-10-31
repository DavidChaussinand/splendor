from django.db import models


# Create your models here.


class StockDB(models.Model):
    red = models.IntegerField(default=0)
    # green = models.IntegerField(default=0)
    # blue = models.IntegerField(default=0)
    # black = models.IntegerField(default=0)
    # white = models.IntegerField(default=0)


class BoardDB(models.Model):
    # yellow = models.IntegerField(default=5)
    stock = models.ForeignKey(StockDB, on_delete=models.CASCADE)
    # noble_number = models.IntegerField(default=0)
    # card_level1 = models.IntegerField(default=0)
    # card_level2 = models.IntegerField(default=0)
    # card_level3 = models.IntegerField(default=0)
    # cards = models.JSONField


class GameDB(models.Model):
    board = models.ForeignKey(BoardDB, on_delete=models.CASCADE)


class PlayerDB(models.Model):
    # yellow = models.IntegerField(default=0)
    stock = models.ForeignKey(StockDB, on_delete=models.CASCADE)
    game = models.ForeignKey(GameDB, on_delete=models.CASCADE)
    # noble_number = models.IntegerField(default=0)
    # cards = models.JSONField
    # cards_reserved = models.JSONField
