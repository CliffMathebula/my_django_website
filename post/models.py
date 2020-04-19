from django.db import models
from django.urls import reverse 



class Post(models.Model):
    name = models.TextField(max_length=100)
    surname = models.TextField(max_length=100,default=None)
    UserName = models.CharField(max_length = 100, default=None)
    id_number = models.IntegerField(default=None)
    Email = models.EmailField(default=None, max_length = 100)
    CellNumber = models.CharField(max_length=20, default=None)
    Address = models.TextField(default=None, max_length= 250)
    PostalCode = models.IntegerField(default=None)
    PassWord = models.CharField(max_length=250, default=None)


    def __str__(self):
    
        return self.name
        

    def get_absolute_url(self): # new
        return reverse('user_details', args=[str(self.pk)])

    