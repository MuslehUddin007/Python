from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse("<h1>Md Musleh Uddin Khan</h1>")

def about(request):
    return HttpResponse('''<a href="https://www.facebook.com/who.agent.007"> About Md Musleh Uddin Khan </a></br><a href="/">Back</a>''')


def analyze(request):
    djtext = request.POST.get('text','default')         #get the text from web input
    removepunc = request.POST.get('removepunc','off')  #check checker on or off default off
    fullcaps = request.POST.get('fullcaps','off')      #check checker on or off default off
    removenewline = request.POST.get('removenewline','off')
    charcount = request.POST.get('charcount','off')
    analyzed = ""
    if (removepunc=="on" and fullcaps=="on"):          #remove punc and change to upper case
        punctuationsList = '''!~()-=[]{};:'"\|<>,./?@#$%^&*'''
        for char in djtext:
            if char not in punctuationsList:
                analyzed +=char.upper() 
        anal = {'purpose':'Removed Punctuations and Change to upper case','analyzed_text':analyzed}
        return render(request,'analyze.html',anal)    #retur webapp the result
    elif fullcaps =="on":                            #chage to upper case
        #analyzed = ""
        for char in djtext:
            analyzed += char.upper() 
        anal = {'purpose':'Change to upper case','analyzed_text':analyzed}
        return render(request,'analyze.html',anal)
    elif removenewline == "on":
        for char in djtext:
            if char != "\n":
                analyzed += char
        anal = {'purpose':'Remove new Line','analyzed_text':analyzed}
        return render(request,'analyze.html',anal)
    elif removepunc=="on":                           #remove punc
        punctuationsList = '''!~()-=[]{};:'"\|<>,./?@#$%^&*'''
        for char in djtext:
            if char not in punctuationsList:
                analyzed += char
        anal = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',anal)
    elif charcount == "on":
        a = 0
        for char in djtext:
            if not(char == " "):
                a = a + 1
        anal = {'purpose':'Count Char','analyzed_text':a}
        return render(request,'analyze.html',anal)
    else:
        return HttpResponse('Error, Click on any checkbox and TRY AGAIN')
    