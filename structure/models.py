# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

# Create your models here.
class InputDeckstring(forms.Form):
    deckstring = forms.CharField(widget = forms.TextInput())
