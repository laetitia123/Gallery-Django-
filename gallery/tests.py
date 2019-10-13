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

   def test_delete_method(self):
      
       self.image.save_image()
       self.image.delete_image()

 
   def test_get_image_by_id(self):
       
       self.image.save_image()
       this_img= self.image.get_image_by_id(self.image.id)
       image = Image.objects.get(id=self.image.id)
       self.assertTrue(this_img, image)

   def test_filter_by_location(self):
       
       self.image.save_image()
       this_img = self.image.filter_by_location(self.image.location_id)
       image = Image.objects.filter(location=self.image.location_id)
       self.assertTrue(this_img, image)
# # ............................testing location model........................................
# class LocationTestClass(TestCase):
#     def setUp(self):
#         self.kigali = Location(location='kigali')
#         self.kigali.save_location()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.kigali,Location))
    
#     def test_updating_location(self):
#         location = Location.get_location_id(self.kigali.id)
#         location.update_location('kigali')
#         location = Location.get_location_id(self.kigali.id)
#         self.assertTrue(location.location == 'kigali')
    
#     def tearDown(self):
#         self.kigali.delete_location()
#         # ......................................test location model............
# class CategoryTestClass(TestCase):
#     def setUp(self):
#         self.food = Category(category='food')
#         self.food.save_category()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.food,Category))
    
#     def tearDown(self):
        self.food.delete_category()
 