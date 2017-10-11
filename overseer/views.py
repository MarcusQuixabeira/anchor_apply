# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import AvaliationForm
from .models import Avaliation

# Create your views here.
def index(request):
    return render(request, 'overseer/index.html')

def process(request):
    if request.method == 'POST':
        if request.FILES:
            form = AvaliationForm(request.POST, request.FILES)
            if form.is_valid():
                avaliation = Avaliation(upload=request.FILES['upload'])
                avaliation.process()
                avaliation.save()
                return HttpResponseRedirect(reverse('overseer:result', args=(avaliation.id,)))
        else:
            return HttpResponseRedirect(reverse('overseer:index'))

def result(request, avaliation_id):
    avaliation = get_object_or_404(Avaliation, pk=avaliation_id)
    return render(request, 'overseer/result.html', {'avaliation': avaliation})
