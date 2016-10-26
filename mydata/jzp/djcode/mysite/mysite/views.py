from django.http import HttpResponse
import datetime
from django.contrib import auth
from django.template import RequestContext
from django.http  import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt



def current_time(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def hours_ahead(request,offset):
	offset = int(offset)
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s),it will be %s.</body></html>" % (offset,dt)
	return HttpResponse(html)

'''
def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index/')

	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username,password=password)

	if user is not None and user.is_active:
		auth.login(request,user)
		return HttpResponseRedirect('/index/')
	else:
		return render_to_response('login.html',RequestContext(request,locals()))
'''
@csrf_exempt
def index(request):
	return render_to_response('index.html',RequestContext(request,locals()))

#TemplateView
from django.views.generic.base import View,TemplateView
#class IndexView(TemplateView):
#	template_name='index.html'

#	def get(self,request,*args,**kwargs):
#		context=self.get_context_data(**kwargs)
#		context[request]=request
#		return self.render_to_response(context)


#class IndexView(TemplateView):
#	template_name='index.html'


def register(request):
	if request.method  == "POST":
		form = UserCreationForm(request.POST)
        	if form.is_valid():
	            	user = form.save()
        	    	return HttpResponseRedirect('/accounts/login/')

	else:
        	form = UserCreationForm()
        	return render_to_response('register.html',RequestContext(request,locals()))




