from django.conf.urls.defaults import patterns, include, url
from geoapp.views import main, ajaxmap, autocomplete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geoproj.views.home', name='home'),
    # url(r'^geoproj/', include('geoproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$', main),
    (r'^ajaxmap/(?P<location>.+)/$', ajaxmap),
    (r'^autocomplete/(?P<word>.+)/$', autocomplete),
    
)

urlpatterns += patterns('django.views.static',
    (r'^static_media/(?P<path>.*)$', 
        'serve', {
        'document_root': '/home/watchcat/work/geoproj/geoapp/static',
        'show_indexes': True }),)