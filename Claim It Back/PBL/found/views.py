from django.shortcuts import render ,redirect
from .models import Item
from PBL import views
# Create your views here.
def home(request):
    if request.method=="POST":
        name = request.POST.get('name')
        detail = request.POST.get('details')
        image = request.FILES.get('image')

        item = Item(
            name = name,
            detail = detail,
            image = image,
        )

        item.save()
        return redirect('home')

    return render(request,"reportFound.html" )
