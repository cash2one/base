from django.conf.urls  import *
from django.contrib.auth.decorators import login_required
import restaurants
from  restaurants.views import *

urlpatterns = patterns('',
    

    url(r'^welcome/$', welcome),
   # url(r'^list/$', list_restaurants),
    url(r'^list/$', login_required(restaurants.views.RestaurantsView.as_view())),
    url(r'^menu/$', menu),
   # url(r'^menu/$', restaurants.views.FoodView.as_view(),name='FoodView'),
    url(r'^comment/(\d{1,5})/$', comment1),


)
