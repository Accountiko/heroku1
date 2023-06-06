from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Cover(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title
    

class WhyChoose(models.Model):
    title = models.TextField(help_text="use | for next line")
    description = models.TextField(help_text="use | for next line . Only 4 lines allowed")


    def __str__(self):
        return self.title
    
    def get_whychoose_titles_list(self):
        if self.title:
            return self.title.split('|')
        else:
            return None
    
    def get_whychoose_descriptions_list(self):
        if self.description:
            return self.description.split('|')
        else:
            return None
        

        
class Testimonial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    client_name = models.TextField(help_text="use | for next line")
    client_position = models.TextField() 
    client_reviews = models.TextField(help_text="use | for next line . Only 6 lines allowed")


    def __str__(self):
        return self.title
    
    def get_client_name_list(self):
        if self.client_name:
            return self.client_name.split('|')
        else:
            return None
    
    def get_client_position_list(self):
        if self.client_position:
            return self.client_position.split('|')
        else:
            return None
        
    def get_client_reviews_list(self):
        if self.client_reviews:
            return self.client_reviews.split('|')
        else:
            return None
    

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title

class WorkHistory(models.Model):
    counts_title = models.TextField()
    counts_number  = models.TextField()
    img = models.ImageField(upload_to='workshostory',blank=True,null=True)

    def __str__(self):
        return self.counts_title

    


class Client(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='clients')

    def __str__(self):
        return self.title



class HomePage(models.Model):
    cover = models.ForeignKey(Cover,on_delete=models.CASCADE)
    why_choose = models.ForeignKey(WhyChoose,on_delete=models.CASCADE)
    about_us = models.ForeignKey(AboutUs,on_delete=models.CASCADE)
    testimonial = models.ForeignKey(Testimonial,on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)
    work_history = models.ManyToManyField(WorkHistory)


    def __str__(self):
        return "home page details"
 

class Contact(models.Model):
    address  =models.TextField()
    email = models.EmailField(blank=True,null=True)
    Mobile_number = models.PositiveBigIntegerField(validators=[MaxValueValidator(9999999999)])
    alternative_number = models.PositiveBigIntegerField(blank=True,null=True,validators=[MaxValueValidator(9999999999)])
    Whatsapp_number = models.PositiveBigIntegerField(validators=[MaxValueValidator(9999999999)])
    location_url = models.TextField(blank=True,null=True)
    facebook_url = models.TextField()
    twitter_url = models.TextField(blank=True,null=True)
    instagram_url = models.TextField()
    linkedin_url = models.TextField(blank=True,null=True)

    
    def __str__(self):
        return "conatct details"