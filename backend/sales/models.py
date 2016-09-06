from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sales(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    neighborhood = models.CharField(max_length=255)
    year = models.CharField(max_length=30, blank=True)
    #zillow = ForeignKey('self',on_delete=modes. PROTECT)
    type_of_home = models.PositiveSmallIntegerField(null = True)
    num_of_sales = models.PositiveSmallIntegerField(null = True)
    lowest_sale_price =models.FloatField(null = True)
    avg_sale_price = models.FloatField(null = True)
    med_sale_price = models.FloatField(null = True)
    high_sale_price = models.FloatField(null = True)
