from django.shortcuts import render
from found.models import Item


def home(request):
    items = Item.objects.all()
    return render(request, 'home.html',{"items":items})

def reportFound(request):
    return render(request, 'reportFound.html' )