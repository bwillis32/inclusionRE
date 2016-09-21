from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Property(models.Model):
  id = models.AutoField(primary_key = True)
  streetAddress = models.CharField(max_length=200)
  borough = models.CharField(max_length=65)
  state = models.CharField(max_length= 65)
  zip = models.PositiveSmallIntegerField()

  def __str__(self):
    return '{}'.format(self.streetAddress)


class Sales(models.Model):
  id = models.IntegerField(default=0, primary_key=True)
  neighborhood = models.CharField(max_length=255)
  year = models.CharField(max_length=30, blank=True)
  type_of_home = models.PositiveSmallIntegerField(null = True)
  num_of_sales = models.PositiveSmallIntegerField(null = True)
  lowest_sale_price =models.FloatField(null = True)
  avg_sale_price = models.FloatField(null = True)
  med_sale_price = models.FloatField(null = True)
  high_sale_price = models.FloatField(null = True)
  link = models.ForeignKey('appreciation.Property', related_name='Sales')


  def __str__(self):
    return '{}'.format(self.neighborhood)

