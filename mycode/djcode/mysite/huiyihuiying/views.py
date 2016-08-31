#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.contrib import auth
from django.template import RequestContext
from django.http  import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from huiyihuiying.models import *

# Create your views here.



def index(request):
	lanmu = Channel.objects.all().order_by('-sort')
	return render_to_response('hyhy_index.html',RequestContext(request,locals()))
def new(request,lid):
	lanmu = Channel.objects.all().order_by('-sort')
	
	if lid == '7':
		cname='慧影故事'
	elif lid == '8':
		cname='慧影科普'	
	elif lid == '9':
		cname='慧影患者'	
	elif lid == '10':
		cname='慧影名师'	
	elif lid == '11':
		cname='慧影案例'
	elif lid == '12':
		cname='慧影之声'
	else:
		cname = '慧影医疗'

	
	if lid:
		a = Article.objects.filter(channel=lid)
		current_lanmu = Channel.objects.get(id=lid)
	else:
		return HttpResponseRedireced("/hyhy/index/")
	return render_to_response('hyhy_list.html',RequestContext(request,locals()))




def article(request,aid):
	lanmu = Channel.objects.all().order_by('-sort')
	

	if aid:
		a = Article.objects.get(id=aid)
		current_lanmu = Channel.objects.get(id=aid)
	else:
		return HttpResponseRedireced("/hyhy/index/")
	return render_to_response('hyhy_details.html',RequestContext(request,locals()))






	
	if lid:
		a = Article.objects.filter(channel=lid)
		current_lanmu = Channel.objects.get(id=lid)
	else:
		return HttpResponseRedireced("/hyhy/index/")
	return render_to_response('hyhy_list.html',RequestContext(request,locals()))




def article(request,aid):
	lanmu = Channel.objects.all().order_by('-sort')
	

	if aid:
		a = Article.objects.get(id=aid)
		current_lanmu = Channel.objects.get(id=aid)
	else:
		return HttpResponseRedireced("/hyhy/index/")
	return render_to_response('hyhy_details.html',RequestContext(request,locals()))
	if lid:
		a = Article.objects.filter(channel=lid)
		current_lanmu = Channel.objects.get(id=lid)
	else:
		return HttpResponseRedireced("/hyhy/index/")
	return render_to_response('hyhy_list.html',RequestContext(request,locals()))




def article(request,aid):
	lanmu = Channel.objects.all().order_by('-sort')
	

	if aid:
		a = Article.objects.get(id=aid)
		current_lanmu = Channel.objects.get(id=aid)
	else:
		return HttpResponseRedireced("/hyhy/index/")
	return render_to_response('hyhy_details.html',RequestContext(request,locals()))
	if lid:
		a = Article.objects.filter(channel=lid)
		current_lanmu = Channel.objects.get(id=lid)
	else:
		return HttpResponseRedireced("/hyhy/index/")
	return render_to_response('hyhy_list.html',RequestContext(request,locals()))




def article(request,aid):
	lanmu = Channel.objects.all().order_by('-sort')
	

	if aid:
		a = Article.objects.get(id=aid)
		current_lanmu = Channel.objects.get(id=aid)
	else:
		return HttpResponseRedireced("/hyhy/index/")
	return render_to_response('hyhy_details.html',RequestContext(request,locals()))
	if lid:
		a = Article.objects.filter(channel=lid)
		current_lanmu = Channel.objects.get(id=lid)
	else:
		return HttpResponseRedireced("/hyhy/index/")
	return render_to_response('hyhy_list.html',RequestContext(request,locals()))




def article(request,aid):
	lanmu = Channel.objects.all().order_by('-sort')
	

	if aid:
		a = Article.objects.get(id=aid)
		current_lanmu = Channel.objects.get(id=aid)
	else:
		return HttpResponseRedireced("/hyhy/index/")
	return render_to_response('hyhy_details.html',RequestContext(request,locals()))

