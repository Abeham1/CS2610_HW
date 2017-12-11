from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Conversion(models.Model):
    name = models.CharField(max_length=20)
    rate = models.FloatField()
    
    def __str__(self):
        return self.name
        
        