from django.conf.urls  import *

from huiyihuiying.views import *
from django.contrib.auth.views import login

urlpatterns = patterns('',


    url(r'^index/$', index),
    url(r'^new/(\d+)/$',new),
    url(r'^article/(\d+)/$',article),
    #url(r'^login/$', login),
    #url(r'^articles_lists/$',articles_lists),
    #url(r'^articles_list/(\d{1,5})$',articles_list),
    #url(r'^articles_details/(\d{1,5})/$',articles_details),


    #url(r'^comment/(\d{1,5})/$', comment1),
)
