from django import template

register = template.Library()

@register.filter(name='zips',is_safe=True)
def zips(a, b):
  return zip(a, b)

@register.simple_tag
def ziped3(a,b,c):
  return zip(a,b,c)