# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render,redirect

# Create your views here.
from django.http  import HttpResponse
import datetime as dt
from .models import Image

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def gallery(request):
   
    gallery = Image.get_all_images()
    return render(request, 'all-gallery/today-gallery.html', {"gallery":gallery})
 
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-gallery/image.html", {"image":image})
def filter_by_location(request,location_id):
   
   images = Image.filter_by_location(id=location_id )
   return render (request,"all-gallery/location.html", {"images":images})

