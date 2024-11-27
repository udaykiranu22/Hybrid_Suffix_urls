from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def processor(request):
    return HttpResponse('''
    <h1>1. snapdragon</h1>
    <h1>2. mediatech</h1>
    ''')

def display(request):
    return HttpResponse('''
    <h1>this are the display iqoo used.</h1>
    <h1>1. AMOLED</h1>
    <h1>2. LCD</h1>
    ''')
