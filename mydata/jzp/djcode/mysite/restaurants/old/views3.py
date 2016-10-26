#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from restaurants.models import Restaurant,Food,Comment
from django.template import RequestContext
from django.utils import timezone
# Create your views here.

def welcome(request):
	restaurants = Restaurant.objects.all()

	if "user_name" in request.POST and request.POST['user_name'] != "":
		user_name = request.POST['user_name']
		return render_to_response('restaurants_list.html',RequestContext(request,locals()))

	else:
		return render_to_response('welcome.html',RequestContext(request,locals()))



def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('restaurants_list.html',locals())



def menu(request):
	if 'id' in request.GET and request.GET['id'] !='':
		restaurant = Restaurant.objects.get(id=request.GET['id'])
		return render_to_response('food_list.html',locals())
	else:
		return HttpResponseRedirect("/list/")



def  comment(request,id):
                if id:
                        r = Restaurant.objects.get(id=id)
                else:
                        return HttpResponseRedirect("/list/")

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



def comment1(request,id):
	if id:
		r = Restaurant.objects.get(id=id)
	else:
		return HttpResponseRedireced("/list/")

	errors = []
	if request.POST:
		visitor=request.POST['visitor']
		email=request.POST['email']
		content=request.POST['content']
		date_time=timezone.localtime(timezone.now())
		if any(not request.POST[k] for k in request.POST):
			errors.append('*表单输入不完整，请重新输入。')

		if not '@' in email:
			errors.append('*邮箱格式不正确，请重新输入。')
		if not errors:
			Comment.objects.create(visitor=visitor,
						email=email,
						content=content,
						date_time=date_time,
						restaurant=r	
)

	return render_to_response('comments.html',RequestContext(request,locals()))
