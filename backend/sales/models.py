from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sales(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    neighborhood = models.CharField(max_length=255)
    
    
