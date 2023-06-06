from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.




def blog(request):
    blog = Blog.objects.all()
    context = {"blog":blog}
    return render(request,'blog.html',context)


def blog_details(request,slug):
    blogs = get_object_or_404(Blog,slug=slug)
    context = {"blogs":blogs}
    return render(request,'blog_details.html',context)

