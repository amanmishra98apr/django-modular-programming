from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showBranch(request):
    return HttpResponse("I'm from CS Branch")

