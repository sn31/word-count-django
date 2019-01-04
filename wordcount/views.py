from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def count(request):
    fulltext = request.GET["fulltext"]
    count_dict = {}
    for word in fulltext.lower().strip().split():
        if word.lower() in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

    return render(request, "count.html", {"count_dict": list((count_dict).items())})
