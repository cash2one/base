from django.conf.urls  import *

from demo.views import *



urlpatterns = patterns('',


   url(r'^test1',demo_test1.as_view()),
   # url(r'^test1',demo_test1),
   # url(r'^list/$', list_restaurants),
   # url(r'^menu/$', menu),
   # url(r'^comment/(\d{1,5})/$', comment1),


)

