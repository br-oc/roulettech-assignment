# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import requests
import random

chars = ["Lucy", "Whiskers", "Snickers", "Midnight",
         "Felix", "Dusty", "Snuggles", "Oliver",
         "Molly", "Bella", "Lucky", "Zoey",
         "Peanut", "Spooky", "Mittens", "Sugar",
         "Harley", "Sheba", "Bandit", "Jack"]

# Create your views here.

def pixel_art(request):
    url = "https://api.dicebear.com/9.x/pixel-art/svg?seed="
    header = {
    "Content-Type":"image/svg+xml",
    }
    result = requests.get(url + chars[random.randint(0, len(chars) - 1)], headers=header)
    if result.status_code == 200:
        return HttpResponse(result, content_type='image/svg+xml')
    return HttpResponse('ERROR')

def useless_fact(request):
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    result = requests.get(url)
    if result.status_code == 200:
        return HttpResponse(result)
    return HttpResponse(result)
