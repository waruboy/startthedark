from django.conf.urls import patterns, include, url
from django.auth.decorators import login_required
from django.auth.models import User
from django.views.generic.list_detail import object_list
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'startthedark.views.home', name='home'),
    # url(r'^startthedark/', include('startthedark.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^accounts/latest/$', login_required(object_list),
        {'queryset':User.objects.order_by('-date_joined'),
         'paginate_by':50, 'allow_empty':True},
        name='user_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include('events.urls')),
    url(r'^friends/', include('socialgraph.urls')),
)
