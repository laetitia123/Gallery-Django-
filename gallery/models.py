
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
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
  


class Location(models.Model):
    location= models.CharField(max_length =30)
    
    def __str__(self):
         return self.location
    class Meta:
        ordering = ['location']
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    def update_location(self, update):
        self.location = update
        self.save()  

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate


class Image (models.Model):

    name= models.CharField(max_length =30)
    description= models.TextField()
    category = models.ForeignKey(Category)
    location= models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.name  

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def get_all_images(cls):
        image = cls.objects.all()
        return image 
  
    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.get(id=id)
        return image
    @classmethod
    def search_by_category(cls,search_term):
        image= cls.objects.filter(category__category__contains=search_term)
        return image 
    
    @classmethod
    def filter_by_location(cls, id):
       images = Image.objects.filter(location_id=id)
       return images 
     
       