from django.contrib import admin
from .models import *
from django.conf import settings
# Register your models here.
admin.site.site_header = 'Accountkio Dashboard'



class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','is_featured')
    search_fields = ['title',]



admin.site.register(Pages,PageAdmin)
admin.site.register(Definition)
admin.site.register(HowToRegister)
admin.site.register(DocumentsRequired)
admin.site.register(Eligibility)
admin.site.register(FAQ)
admin.site.register(SplitFace)
admin.site.register(Cards)
admin.site.register(Category)