from django.http import HttpResponse # used to pass info to views

import random

#view function
def hello_world(request):
    return HttpResponse("Hello World")

