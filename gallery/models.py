# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime as dt

# Create your models here.
from django.db import models

class Category(models.Model):
    category= models.CharField(max_length =30)
   
    def __str__(self):
         return self.category
    class Meta:
        ordering = ['category']
class Image (models.Model):
    post = models.TextField()
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_image = models.ImageField(upload_to = 'images/')
   
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    