# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from . import models

# Create your views here.
def input_deckstring(request):
    if request.method == 'POST':
        form = InputDeckstring(request.POST)
        if form.is_valid():
            return HttpResponse(request, 'input_deckstring.html')
    else:
        form = InputDeckstring()
        context = {'form':form}
        return render(request, 'main.html') #??????

def index(request):
    return HttpResponse("Hello, welcome to this shitty app.")
