from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import current_time, hours_ahead
#from students.views import stu
import ckeditor
import views
#from restaurants.views import welcome, list_restaurants, menu, comment,comment1
#import restaurants


from books.views import search

#from views import index,register
import mysite.views

from articles.views import index
from django.contrib.auth.views import login
from django.views.generic.base import TemplateView



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
    #test
    url(r'^time/$', current_time),
    url(r'^time/plus/(\d{1,2})$', hours_ahead),

    #student
    url(r'^stu/', include('students.urls')),


    #books
    url(r'^search/$', search),
    
    #admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    

    #restaurants
    #url(r'^welcome/$', welcome),
    #url(r'^list/$', list_restaurants),
    #url(r'^menu/$', menu),
    #url(r'^comment/(\d{1,5})/$', comment1),
    url(r'^res/',include('restaurants.urls')),

    #views
    #url(r'^accounts/register/$', register),
    #url(r'index/$', index),

    #articles
    url('^articles/',include('articles.urls')),
    url('^ckeditor/',include('ckeditor.urls')),
    #url(r'^',index ),

    #demo
    url(r'^demo/',include('demo.urls')),
    
    #huiyihuiying
    url(r'^hyhy/',include('huiyihuiying.urls')),
    
)

urlpatterns += patterns('mysite.views',

    url(r'^accounts/register/$','register'),
    #url(r'^index/$','index'),			
    #url(r'^index/$',views.IndexView.as_view()),			
    url(r'^index/$',TemplateView.as_view(template_name='index.html')),			


    
)



from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)


