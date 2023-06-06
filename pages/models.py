from django.db import models
from django.utils.text import slugify 
from django.urls import reverse
# Create your models here.


class Definition(models.Model):
    title = models.CharField(max_length=255)
    definition = models.TextField()


    def __str__(self):
        return self.title

class HowToRegister(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    card_titles = models.TextField(help_text="use | for next line" , )
    card_descriptions = models.TextField(help_text="use | for next line . must same line as card-title" )
    
    
    def __str__(self):
        return self.title
    
    def get_card_titles_list(self):
        if self.card_titles:
            return self.card_titles.split('|')
        else:
            return None
    
    def get_card_descriptions_list(self):
        if self.card_descriptions:
            return self.card_descriptions.split('|')
        else:
            return None
    
    
class DocumentsRequired(models.Model):
    title = models.CharField(max_length=255)
    documents= models.TextField(help_text="use | for next line")

    def __str__(self):
        return self.title
    
    def get_documents_list(self):
        if self.documents:
            return self.documents.split('|')
        else:
            return None
    


class Eligibility(models.Model):
    title = models.CharField(max_length=255)
    eligibilities = models.TextField(help_text="use | for next line")

    def __str__(self):
        return self.title
    def get_eligibilities_list(self):
        if self.eligibilities:
            return self.eligibilities.split('|')
        else:
            return None

class FAQ(models.Model):
    title = models.CharField(max_length=255)
    questions = models.TextField(help_text="use | for next line")
    answers = models.TextField(help_text="use | for next line")
    count = 0
    def __str__(self):
        return self.title
    
    def get_questions_list(self):
        if self.questions:
            return self.questions.split('|')
        else:
            return None
    
    def get_answers_list(self):
        if self.answers:
            return self.answers.split('|')
        else:
            return None
    
    def get_number(self):
        num = range(0,len(self.questions.split('|')))
        return num





# extra fields
class SplitFace(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    points = models.TextField(help_text="use | for next line",blank=True,null=True)
    extras = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title
    
    def get_points_list(self):
        return self.points.split('|')
    
    
    


class Cards(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    card_titles = models.TextField(help_text="use | for next line",blank=True,null=True)
    card_descriptions = models.TextField(help_text="use | for next line",blank=True,null=True)

    def __str__(self):
        return self.title
    def get_card_title_list(self):
        return self.card_titles.split('|')
    
    def get_card_descriptions_list(self):
        return self.card_descriptions.split('|')


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title + " " + str(self.id)


class Pages(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    title_description = models.TextField(help_text="use | for next line",max_length=255,null=True,blank=True,default="Contact for details|") # change into list in templtes
    definition = models.ForeignKey(Definition,on_delete=models.CASCADE,null=True,blank=True)
    how_to_register = models.ForeignKey(HowToRegister,on_delete=models.CASCADE,null=True,blank=True)
    documents_required = models.ForeignKey(DocumentsRequired,on_delete=models.CASCADE,null=True,blank=True)
    eligibility = models.ForeignKey(Eligibility,on_delete=models.CASCADE,null=True,blank=True)
    faq = models.ForeignKey(FAQ,on_delete=models.CASCADE,null=True,blank=True)
    extra_split_faces = models.ManyToManyField(SplitFace,blank=True)
    extra_cards = models.ManyToManyField(Cards,blank=True)
    is_featured = models.BooleanField(default=False)
    is_usefull = models.BooleanField(default=False) 
    slug = models.SlugField(null=True,blank=True,help_text="if leave it will take from title ",unique=True)
   
   #for meta datas
    meta_title = models.CharField(max_length=255,null=True,blank=True,help_text="if leave it will take from title ")
    meta_description = models.TextField(null=True,blank=True)
    meta_keywords = models.TextField(null=True,blank=True,help_text="use comma( , ) for separation")


    def save(self, *args, **kwargs):
        if self.slug == None:

            self.slug = slugify(self.title)
        if self.meta_title == None:

            self.meta_title = self.title
        if self.meta_description == None:

            self.meta_description = f"what is {self.title} ?"
        super(Pages, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    
    def get_title_description_list(self):
        if self.title_description:

            return self.title_description.split('|')
        else:
            return None


    def get_absolute_url(self):
    # u create url only here and then reference here throughout of your project
        return reverse("pages",args=[self.slug])



