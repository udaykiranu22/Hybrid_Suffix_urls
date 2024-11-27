from django.urls import path
from iphone.views import *

urlpatterns = [
    path('processor/', processor, name='processor'),
    path('display/', display, name='display'),
]
