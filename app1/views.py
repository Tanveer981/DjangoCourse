from django.shortcuts import render

# create your views here .
from django.http import HttpResponse


def home(request):
    return render(request, 'a.html',{'titles':'Django','link':'http://127.0.0.1:8000/'})
def profile(request):
    return HttpResponse ("profile page")
def expression(request):
    a=(request.POST['text1'])
    b=(request.POST['text2'])
    c=a+b
    return render(request,'output.html',{'result':c})
