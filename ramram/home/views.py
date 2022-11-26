from django.shortcuts import render
from .models import InstaPhoto
import requests

from django.views.generic import TemplateView

# Create your views here.


def index(request):
    context = InstaPhoto.objects.all()
    return render(request, 'home/index.html', context={'context': context})


def refresh(request):
    # ramona page id = 292413182
    requests.get(//graph.facebook.com/{api-version}/292413182/media)
    index(request)
