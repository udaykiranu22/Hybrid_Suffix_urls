from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def processor(request):
    return HttpResponse('''
    <h1>1. Exynos</h1>
    <h1>2. snapdragon</h1>
    <h1>3. mediatech</h1>
    ''')

def display(request):
    return HttpResponse('''
    <h1>this are the display samsung used.</h1>
    <h1>1. AMOLED</h1>
    <h1>2. LCD</h1>
    ''')

