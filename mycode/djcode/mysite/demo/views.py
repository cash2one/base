from django.shortcuts import render_to_response

# Create your views here.


from django.views.generic import View


#def demo_test1(request):
#	bools = True
#        return render_to_response('demo_test.html',locals())


class demo_test1(View):
	def get(self,request):	
		bools = False
		return render_to_response('demo_test.html',locals())


