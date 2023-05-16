from django import template

register = template.Library()

@register.filter(name='zips',is_safe=True)
def zips(a, b):
  return zip(a, b)

