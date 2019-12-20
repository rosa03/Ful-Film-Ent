from django.db import models

# Create your models here.

class Social(models.Model):
    
    link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)

    def __str__(self):
        return self.link

class BlogPost(models.Model):

    title = models.CharField(max_length=200, help_text='Enter title')

    description = models.TextField(max_length=1000, help_text='Enter a brief description')

    link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)

    # image = models.ImageField(upload_to='documents/')

    # video = 

    def __str__(self):
        return self.title


class Member(models.Model):
    
    name = models.CharField(max_length=200, help_text='Enter a name')

    description = models.TextField(max_length=1000, help_text='Enter a brief description')

    socials = models.ManyToManyField(Social, help_text='Enter Socials')

    def __str__(self):
        return self.name

    def display_socials(self):
        return ', '.join(socials.link for socials in self.socials.all()[:3])

    display_socials.short_description = 'Socials'