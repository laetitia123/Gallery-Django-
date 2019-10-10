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