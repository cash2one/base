from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.contrib import auth
from django.template import RequestContext
from django.http  import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from articles.models import *

# Create your views here.



def register(request):
	if request.method  == "POST":
		form = UserCreationForm(request.POST)
        	if form.is_valid():
	            	user = form.save()
        	    	return HttpResponseRedirect('/articles/index/')

	else:
        	form = UserCreationForm()
        	return render_to_response('register.html',RequestContext(request,locals()))


def index(request):
	classes = Classes.objects.all()
	return render_to_response('articles_index.html',RequestContext(request,locals()))



#def articles_list(request):
#	articles = Article.objects.all()
#	return render_to_response('articles_list.html',RequestContext(request,locals()))

def articles_lists(request):
	classes = Classes.objects.all()
	articles = Article.objects.all()
	return render_to_response('articles_list.html',RequestContext(request,locals()))

def articles_list(request,id):
	classes = Classes.objects.all()
        if id:
		c = Classes.objects.get(id=id)
		articles = Article.objects.filter(classes=c)

	else:
		return HttpResponseRedireced("/articles/index/")
	
        return render_to_response('articles_list.html',RequestContext(request,locals()))



def articles_details(request,id):
	classes = Classes.objects.all()
	if id:
		a = Article.objects.get(id=id)
	else:
		return HttpResponseRedireced("/articles/articles_list/")

	return render_to_response('articles_details.html',RequestContext(request,locals()))
