from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Conversion(models.Model):
    value = models.FloatField()
    unit1 = models.CharField(max_length=20)
    unit2 = models.CharField(max_length=20)
    
    def __str__(self):
        return self.unit1 + " to " + self.unit2
        
        
        
#API key: jNwh_nS1XpvJfiJZFaFV