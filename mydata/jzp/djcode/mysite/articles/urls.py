from django.conf.urls  import *

from articles.views import *
from django.contrib.auth.views import login

urlpatterns = patterns('',


    url(r'^index/$', index),
    url(r'^register/$',register),
    url(r'^login/$', login),
    url(r'^articles_lists/$',articles_lists),
    url(r'^articles_list/(\d{1,5})$',articles_list),
    url(r'^articles_details/(\d{1,5})/$',articles_details),


   # url(r'^comment/(\d{1,5})/$', comment1),
)
