from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zqxt_views.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/$', 'calc.views.add', name = 'add'),
    url(r'^add/(\d+)/(\d+)/$', 'calc.views.add2', name = 'add2'),
    url(r'^$', 'calc.views.index', name='home'),
)
