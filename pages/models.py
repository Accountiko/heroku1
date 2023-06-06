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
        return self.card_titles.split('|')
    
    def get_card_descriptions_list(self):
        return self.card_descriptions.split('|')
    
    
class DocumentsRequired(models.Model):
    title = models.CharField(max_length=255)
    documents= models.TextField(help_text="use | for next line")

    def __str__(self):
        return self.title
    
    def get_documents_list(self):
        return self.documents.split('|')
    


class Eligibility(models.Model):
    title = models.CharField(max_length=255)
    eligibilities = models.TextField(help_text="use | for next line")

    def __str__(self):
        return self.title
    def get_eligibilities_list(self):
        return self.eligibilities.split('|')

class FAQ(models.Model):
    title = models.CharField(max_length=255)
    questions = models.TextField(help_text="use | for next line")
    answers = models.TextField(help_text="use | for next line")
    count = 0
    def __str__(self):
        return self.title
    
    def get_questions_list(self):
        return self.questions.split('|')
    
    def get_answers_list(self):
        return self.answers.split('|')
    
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
        return self.title


class Pages(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    title_description = models.TextField(help_text="use | for next line",max_length=255) # change into list in templtes
    definition = models.ForeignKey(Definition,on_delete=models.CASCADE)
    how_to_register = models.ForeignKey(HowToRegister,on_delete=models.CASCADE)
    documents_required = models.ForeignKey(DocumentsRequired,on_delete=models.CASCADE)
    eligibility = models.ForeignKey(Eligibility,on_delete=models.CASCADE)
    faq = models.ForeignKey(FAQ,on_delete=models.CASCADE)
    extra_split_faces = models.ManyToManyField(SplitFace,blank=True)
    extra_cards = models.ManyToManyField(Cards,blank=True)
    slug = models.SlugField(null=True,blank=True,help_text="if leave it will take from title ",unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Pages, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    
    def get_title_description_list(self):
        return self.title_description.split('|')


    def get_absolute_url(self):
    # u create url only here and then reference here throughout of your project
        return reverse("pages",args=[self.slug])



