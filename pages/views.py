from django.shortcuts import render
from .models import Pages,Category
from django.shortcuts import get_object_or_404
from home.models import Contact,HomePage
# Create your views here.

def home(request):
    page = Pages.objects.filter(is_featured=True)
    contact = Contact.objects.all()
    home = HomePage.objects.all()
    context = {"page":page,'contact':contact,'home':home}
    return render(request,'home.html',context)



def pages(request,slug):
    pages = get_object_or_404(Pages,slug=slug)
    context = {"pages":pages}
    return render(request,'pages.html',context)


