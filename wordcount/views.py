from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def count(request):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    fulltext = request.GET["fulltext"]
    for char in fulltext.lower():
        if char in punctuations:
            fulltext = fulltext.replace(char, " ")
    count_dict = {}
    for word in fulltext.lower().strip().split():
        if word.lower() in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

    word_frequency_sorted = sorted(
        count_dict.items(),
        key=lambda kv: kv[1],
        reverse=True)
    return render(request, "count.html", {"total_count": len(fulltext), "words": word_frequency_sorted, "fulltext": fulltext})
