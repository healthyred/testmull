# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

# Create your models here.
<<<<<<< HEAD
class InputDeckstring(forms.Form):
    deckstring = forms.CharField(widget = forms.TextInput())
=======


class Card(models.Model):
    """
    This is the name of each of the cards in the hand
    """
    card = models.Charfield(max_length=200)

    def __str__(self):
        return self.name

class Simulator(models.Model):
    """
    This is the model which will set up the information that will be dumped
    into the SQL
    """
    deckcode = models.CharField(max_length=200)
    decklist = models.CharField(max_length=200)
    order = models.Charfield(max_length=200)
    opponent = models.Charfield(max_length=200)
    ##Maybe change the many to many to a single charfield depending on how things
    ##look in the actual database
    hand = models.ManyToManyField(Card, through='Card')
    user_selection = models.ManyToManyField(Card, through='Card')
>>>>>>> e8f9adc8edcb32007f560cf0e6ed2449f1cf6a62
