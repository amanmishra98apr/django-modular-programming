from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def showYear(request):
    return HttpResponse("I'm final year student")
