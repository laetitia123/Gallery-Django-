from django.test import TestCase
from .models import Location,Image,Category
import datetime as dt



class ImageTestClass(TestCase):
  
   def setUp(self):
        self.people = Category(category='people')
        self.people.save_category()

        self.kigali = Location(location='kigali')
        self.kigali.save_location()

        self.image = Image(name='amezing', description='group', location=self.kigali, category=self.people)
        self.image.save_image()
   def test_instance(self):
       self.assertTrue(isinstance(self.image, Image))
  def test_save_method(self):
       
       self.image.save_image()
       images = Image.objects.all()
       self.assertTrue(len(images) > 0)

