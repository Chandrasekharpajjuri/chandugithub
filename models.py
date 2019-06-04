from django.db import models
from django.core.exceptions import ValidationError
from django.core import validators
from multiselectfield import MultiSelectField
from django.urls.resolvers import URLResolver as u
from django.urls import reverse

import datetime

year_dropdown = []
for y in range(1950, (datetime.datetime.now().year + 5)):
    year_dropdown.append((y, y))

            
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Curdmodel1(models.Model):
   
    CHOICE=(('Mr','Mr'),
            ('Mrs','Mrs'),('Ms','Ms'))
    
    DISTRIC_CHOICES = [
        ('GNT', 'Guntur'),
        ('SRKLM', 'Srikakulam'),
        ('VNM', 'Vijayanagaram'),
        ('VIZAG', 'Vizag'),
        ('WG','West Godavari'),
        ('EG','East Godavari'),
        ('KRISHNA','Krishna'),
        ('PKSM','Ongol'),
        ('SNLR','Nelor'),
        ('KRNL','Kornool'),
        ('KDP','Kadapa'),
        ('CHT','Chitor'),
        ('ANTP','Ananthapuram'),
    ]

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    MY_CHOICES = [('Py', 'Python'),
              ('Dj', 'Django'),
              ('MySql', 'MySql'),
              ('RestApi', 'RestApi'),
              ('HTML5', 'HTML5'),
              ('CSS5','CSS5'),
              ('MongoDB','MongoDB')
              ]
    year=range(1900,2019)

    Select=models.CharField(max_length=4,choices=CHOICE,default='Mr')
    Ename= models.CharField(max_length=254)
    Subject=models.CharField(max_length=20)
    Sal=models.FloatField()
    Date_of_birth=models.DateField()
    Gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='Male')
    Distric = models.CharField(max_length=10,choices=DISTRIC_CHOICES,default='GUNTUT')
    Technologies = MultiSelectField(choices=MY_CHOICES)
    Search=models.CharField(max_length=200,default='http://')
    File= models.FileField(upload_to='documents/')
    User_Image= models.ImageField(upload_to='images/', null=True, blank=True)
    Passed = models.IntegerField(('year'),choices=year_dropdown, default=datetime.datetime.now().year)
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
    
    
class EmailSendModel(models.Model):
    From=models.EmailField(default='@gmail.com')
    To=models.EmailField(default='@gmail.com')
    Subject = models.CharField(max_length=100)
    Attach= models.FileField(upload_to='senddoc/')
    Message = models.TextField(max_length=250)



class FormSetModel(models.Model):
    Name=models.CharField(max_length=20)
    Date=models.DateField()


    
    
