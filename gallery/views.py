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
    date = dt.date.today()
    gallery = Image.get_all_images()
    return render(request, 'all-gallery/today-gallery.html', {"date": date,"gallery":gallery})
 
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        # message = f"{search_term}"

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
def get_image_by_location(request,loc):
    image = Image.get_image_by_location(loc)
   
    return render(request, 'location.html', {"image": image})


# def single_image(request,image_id):
#     image=Image.objects.get(id = image_id)
#     return render(request, 'image.html',{"image":image})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day
def past_days_news(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Image.days_news(date)
    return render(request, 'all-news/past-news.html',{"date": date,"news":news})