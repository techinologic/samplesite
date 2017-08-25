from django.http import HttpResponse

def index(request):
    return HttpResponse("You are in the polls index.")


# Create your views here.
