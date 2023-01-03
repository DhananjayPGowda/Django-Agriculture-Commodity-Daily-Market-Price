from django.db import models
from django import forms
import datetime
# Create your models here.
class Crop(models.Model):
    name = models.CharField(max_length=40,unique=True)
    img = models.ImageField(default='unknown.jpg') 
    def __str__(self):
        return self.name

class Variety(models.Model):
    name = models.CharField(max_length=25)
    crop = models.ForeignKey(Crop,on_delete = models.CASCADE,related_name = "variety")
    def __str__(self):
        return self.name
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['name','crop'],name = 'unuque variety')
        ]

class Market(models.Model):
    name = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['name','district','district'],name = 'unuque market')
        ]


class Items(models.Model):
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE,related_query_name= 'items')
    variety = models.ForeignKey(Variety,on_delete=models.CASCADE,related_query_name='items')
    market = models.ForeignKey(Market,on_delete=models.CASCADE,related_query_name='items')
    min_price = models.FloatField(default=None)
    max_price = models.FloatField(default=None)
    mod_price = models.FloatField(default=None)
    date = models.DateField(default = datetime.date.today())
    updated_on  = models.DateField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['crop', 'variety', 'market','date'],name='unique item')
        ]
    def __str__(self):
        return self.crop.name