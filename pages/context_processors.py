def categories(request):
    from .models import Category
    from home.models import Contact
    from .models import Pages
    return {'categories': Category.objects.all(),'contact':Contact.objects.all(),"usefull":Pages.objects.filter(is_usefull=True)}