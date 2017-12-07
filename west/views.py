# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_page(request):
    return HttpResponse("<p>西餐</p>")