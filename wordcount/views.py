from django.shortcuts import render
import operator
def setup(request):
    return render(request, 'wordcount/word_setup.html')
# Create your views here.
def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1


    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'wordcount/count.html',
    { 'fulltext':fulltext,'count':len(wordlist),
    'worddictionary':worddictionary, 'worddictionary':worddictionary.items(),
    'sortedwords':sortedwords})
