#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from restaurants.models import Restaurant,Food,Comment
from django.template import RequestContext
from django.utils import timezone
from restaurants.forms import CommentForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User,Permission
from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

def welcome(request):
	restaurants = Restaurant.objects.all()

	if "user_name" in request.POST and request.POST['user_name'] != "":
		user_name = request.POST['user_name']
		return render_to_response('restaurants_list.html',RequestContext(request,locals()))

	else:
		return render_to_response('welcome.html',RequestContext(request,locals()))



#def list_restaurants(request):
#	restaurants = Restaurant.objects.all()
#	return render_to_response('restaurants_list.html',RequestContext(request,locals()))

#DisplayView(ListView DetailView)
from django.views.generic.list import ListView
class RestaurantsView(ListView):
	model=Restaurant
	template_name='restuarants_list.html'
	context_object_name='restaurants'



def menu(request):
	if 'id' in request.GET and request.GET['id'] !='':
		restaurant = Restaurant.objects.get(id=request.GET['id'])
		return render_to_response('food_list.html',RequestContext(request,locals()))
	else:
		return HttpResponseRedirect("/res/list/")

#DetailView
from django.views.generic.detail import DetailView
#class FoodView(DetailView):
#	model=Food
#	template_name='food_ls.html'
#	context_object_name='food'
#	
#	@method_decorator(login_required)
#	def dispatch(self,request,*args,**kwargs):
#		return super(FoodView,self).dispatch(request,*args,**kwargs)	



def  comment(request,id):
                if id:
                        r = Restaurant.objects.get(id=id)
                else:
                        return HttpResponseRedirect("/res/list/")

                if request.POST:
                        visitor = request.POST['visitor']
                        content = request.POST['content']
                        email  = request.POST['email']
                        date_time = timezone.localtime(timezone.now())
                        Comment.objects.create(
                                visitor = visitor,
                                email = email,
                                content=content,
                                date_time=date_time,
                                restaurant = r
                        )
                return render_to_response('comments.html',RequestContext(request,locals()))


@permission_required("restaurants.can_comment",login_url="/accounts/login/")
@csrf_exempt
def comment1(request,id):
	if id:
		r = Restaurant.objects.get(id=id)
	else:
		return HttpResponseRedireced("/res/list/")

	errors = []
	if request.POST:
		visitor=request.POST['visitor']
		email=request.POST['email']
		content=request.POST['content']
		date_time=timezone.localtime(timezone.now())
		f = CommentForm(request.POST)
		if f.is_valid():
			visitor=f.cleaned_data['visitor']
			email=f.cleaned_data['email']
			content=f.cleaned_data['content']
			### 权限验证
			#user = User.objects.get(username=request.user)
			#perm = Permission.objects.get(codename='can_comment')
			#if user.has_perm('restaurants.can_comment'):
			Comment.objects.create(visitor=visitor,
						email=email,
						content=content,
						date_time=date_time,
						restaurant=r	
)
			visitor,email,content=('','','')
			#else:
			#	warm = "您没有权限！"
	else:
		f = CommentForm()
	return render_to_response('comments.html',RequestContext(request,locals()))
