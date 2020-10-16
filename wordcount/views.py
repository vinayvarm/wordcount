from django.http import HttpResponse
from django.shortcuts import render


def sample(request):
    return render(request,'home.html')
def message(request):
    return HttpResponse("message")

def content(request):
    return render(request,'about.html')


def cnt(request):
    text=request.GET['fulltext']
    wordlist= text.split()
    print(len(wordlist))
    dup=[]
    for word in wordlist:
        print(word,wordlist.count(word))
        if wordlist.count(word)>1:
            dup.append(word);
    print(dup)







    return render(request,'count.html',{'tst': text,'wordlist':wordlist,'count':len(wordlist),'duplicates':dup})