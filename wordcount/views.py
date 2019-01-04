from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello")


def egg(request):
    return HttpResponse("Eggs")
