#coding:utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from students.models import Student, School, Grade
# Create your views here.

def stu(request):
	#name = School.objects.all()
#	school = {'name':name,'tel':'1111111111'}
	sear = request.POST.get('sear',None)
	danxuan = str(request.POST.get('danxuan',None))
	if not sear or not danxuan:
		students = Student.objects.all()[0:7]
	elif danxuan=='name':
		students = Student.objects.filter(name__contains=sear)
	elif danxuan=='graduatedfrom':
		students = Student.objects.filter(graduatedfrom__contains=sear)

	return render_to_response('stu_index.html',RequestContext(request,locals()))

