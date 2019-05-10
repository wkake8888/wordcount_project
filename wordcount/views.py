from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def self_introduction(request):
    return render(request, 'about_me.html')


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    word_dictionary = {}
    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    sortedword = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist),
                                          'sortedword': sortedword})
