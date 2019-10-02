

from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    # print("Hallo, hier komt: " + fulltext)
    wordlist = fulltext.split()

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext,
                                          'count': len(wordlist),
                                          'worddictionary': sortedwords})




def eggs():
    return HttpResponse('Eggs are great!!')

def ceggs():
    return HttpResponse('<h1>Eggs are great!!</h1>')

def leggs(request):
    return render(request,'home1.html', {'hithere':'This is me...', 'hiyou':'This is you...' } )

def about(request):
    return render(request, 'about.html')


