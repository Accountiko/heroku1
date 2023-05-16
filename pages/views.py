from django.shortcuts import render
from .models import Pages
from django.shortcuts import get_object_or_404

# Create your views here.



def home(request):
    pages = Pages.objects.all()
    context = {"pages":pages}
    return render(request,'home.html',context)


def pages(request,slug):
    pages = get_object_or_404(Pages,slug=slug)
    context = {"pages":pages}
    return render(request,'pages.html',context)