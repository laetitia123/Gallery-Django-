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
class Location(models.Model):
    location= models.CharField(max_length =30)
    
    
   
    def __str__(self):
         return self.location
    class Meta:
        ordering = ['location']
class Image (models.Model):
    post = models.TextField()
    category = models.ForeignKey(Category)
    location= models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_image = models.ImageField(upload_to = 'images/')
    
    @classmethod
    def get_all_images(cls):
        image = cls.objects.all()
        return image
    @classmethod
    def search_by_category(cls,search_term):
        image= cls.objects.filter(category__icontains=search_term)
        return image 
    
    @classmethod
    def filter_by_location(cls, id):
       images = Image.objects.filter(location_id=id)
       return images  
       

    