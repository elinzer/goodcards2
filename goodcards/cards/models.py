from django.db import models
from user.models import User
# Create your models here.

class Card(models.Model):
    card_name = models.CharField(max_length=200)
    img_url = models.URLField()
    mana_cost = models.CharField(max_length=200)
    text = models.TextField()
    rarity = models.CharField(max_length=200)
    card_set = models.CharField(max_length=200)


class Deck(models.Model):
    deck_name = models.CharField(max_length=200)
    cover_img = models.URLField()
    cards = models.ManyToManyField(Card)
    user = models.ForeignKey(User, on_delete=models.CASCADE)