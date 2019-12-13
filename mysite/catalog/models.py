from django.db import models

# Create your models here.

class Socials(models.Model):
    
    link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)

    def __str__(self):
        return self.link

class BlogPost(models.Model):

    title = models.CharField(max_length=200, help_text='Enter title')

    text = models.TextField(max_length=1000, help_text='Enter a brief description')

    link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)

    # image = models.ImageField(upload_to=)

    # video = 

    def __str__(self):
        return self.title


class Member(models.Model):
    
    name = models.CharField(max_length=200, help_text='Enter a name')

    text = models.TextField(max_length=1000, help_text='Enter a brief description')

    socials = models.ManyToManyField(Socials, help_text='Enter Socials')