from django.test import TestCase
from .models import Location,Image,Category
import datetime as dt



class ImageTestClass(TestCase):
  
   def setUp(self):
        self.people = Category(category='people')
        self.people.save_category()

     