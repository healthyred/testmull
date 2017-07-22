# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#from .forms import TakeDeckstring

# Create your views here.
#def get_deckstring(request):
#    if request.method == 'POST':
#        form = TakeDeckstring(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect('PLACEHOLDER')

#    else:
#        form = TakeDeckstring()

#    return render(request, 'input_deckstring.html', {'form': form})

def index(request):
    return HttpResponse("Hello, welcome to this shitty app.")
