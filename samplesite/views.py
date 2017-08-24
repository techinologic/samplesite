from django.http import HttpResponse # used to pass info to views

import random

#view function
def hello_world(request):
    return HttpResponse("Hello World")

def root_page(request):
    return HttpResponse("Root Homepage")

def random_number(request, max_rand=100):
    random_num = random.randrange(0, int(max_rand))
    msg = "Random number between 0 and %s: %d" % (max_rand, random_num)
    return HttpResponse(msg)

