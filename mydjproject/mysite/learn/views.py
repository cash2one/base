# _*_ coding:utf-8 _*_

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(u"欢迎光临，好好学习，天天向上！")

