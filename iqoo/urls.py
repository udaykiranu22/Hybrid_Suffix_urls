from django.urls import path
from iqoo.views import *

urlpatterns = [
    path('processor/', processor, name='processor'),
    path('display/', display, name='display'),
]