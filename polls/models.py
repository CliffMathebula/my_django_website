import datetime

from django.db import models
from django.utils import timezone


class Registration(models.Model):
    name = models.TextField(max_length=255, null=False)
    surname = models.TextField(max_length=255, null=False)
    id_number = models.IntegerField(null=False)
    cellnumber = models.CharField(max_length=255, null = False)
    date_of_reg = models.DateTimeField(timezone.now)
    
    
    

    def __str__(self):
        return self.name
    