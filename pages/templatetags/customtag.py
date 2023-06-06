from django import template
from django.conf import settings
from pages.models import Pages,Category
from blog.models import Blog
register = template.Library()

@register.filter(name='zips',is_safe=True)
def zips(a, b):
  return zip(a, b)

@register.filter(name='whatsappmsg',is_safe=True)
def whatsappmsg(value):
  msg = settings.WHATSAPP_MSG

  title = value.replace(" ", "%20")
  return msg +" "+ title

@register.filter(name='navbar',is_safe=True)
def navbar(cat):
  changed_list = Pages.objects.filter(category__title=cat)

  return changed_list


@register.filter(name='navbarblog',is_safe=True)
def navbarblog(cat):
  changed_list = Blog.objects.filter(category__title=cat)

  return changed_list

@register.simple_tag
def usefulllinks ():
  pages = Pages.objects.filter(is_featured=True)
  return pages
