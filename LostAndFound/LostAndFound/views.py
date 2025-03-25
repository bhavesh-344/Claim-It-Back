from django.shortcuts import render,redirect
from apps.found.models import Item
from django.contrib.auth.decorators import login_required

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html',{"items":items})

def reportFound(request):
    return render(request, 'reportFound.html' )

@login_required(login_url="login") 
def claimNow(request,id):
    item=Item.objects.filter(id=id).first()
    return render(request,'claimNow.html',{"item":item})