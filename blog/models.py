from django.db import models
from django.utils.text import slugify 
from django.urls import reverse
from ckeditor.fields import RichTextField


from pages.models import Category
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    context = RichTextField()
    date_publish = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True,blank=True,help_text="if leave it will take from title ",unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
    # u create url only here and then reference here throughout of your project
        return reverse("blogs",args=[self.slug])
    
