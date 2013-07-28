""" Python Package Support """
# Not Applicable

""" Django Package Support """
from django.conf.urls import patterns, url, include
from django.contrib import admin

""" Internal imports """
# Not Applicable

"""

 Retribution/urls.py
 
 Author(s)   :      
 Version     : 1.0
 Last Update : 2013-07-27
 Update by   : Matthew J Swann
 
"""


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'term_proc_listings.views.home', name='home'),
    # url(r'^term_proc_listings/', include('term_proc_listings.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
