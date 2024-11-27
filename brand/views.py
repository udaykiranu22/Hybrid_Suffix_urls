from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def mobiles(request):
    return HttpResponse('''
    <h1>this are brands we have</h1>
    <h1>1. samsung</h1>
    <h1>2. iphone</h1>
    <h1>3. iqoo</h1>
    <h1>4. realme</h1>
    <h3>Here we can check processor, display of the mobile brand that used.</h3>
    ''')