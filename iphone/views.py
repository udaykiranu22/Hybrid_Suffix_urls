from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def processor(request):
    return HttpResponse('''
    <h1>1. A-series Bionic chipset</h1>
    ''')

def display(request):
    return HttpResponse('''
    <h1>1.IPHONE USED AMOLED DISPLAY</h1>
    ''')