# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request,'home.html',context)

def add(request):
        a = request.GET['a']
        b = request.GET['b']
        c = int(a) + int(b)
        return HttpResponse(str(c))

