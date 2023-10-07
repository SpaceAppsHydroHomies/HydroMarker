from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(response):
    return JsonResponse({"foo": "barr"})
