from django.conf.urls.defaults import *

from django.contrib import admin
from ajax_select import urls as ajax_select_urls

import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^search_form',  view='views.search_form',name='search_form'),
    (r'^admin/lookups/', include(ajax_select_urls)),
    (r'^admin/', include(admin.site.urls)),

    url(r'person/search/', views.PersonAjaxLookupView.as_view(), name="person-search"),
)
