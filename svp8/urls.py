# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
from django.contrib import auth

import settings
import views


from django_authopenid.urls import urlpatterns as authopenid_urlpatterns
from registration.forms import RegistrationFormUniqueEmail

from djangobb_forum import settings as forum_settings

for i, rurl in enumerate(authopenid_urlpatterns):
    if rurl.name == 'registration_register':
        authopenid_urlpatterns[i].default_args.update({'form_class': RegistrationFormUniqueEmail})
        break

admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    
    url(r'^accounts/login/', auth.views.login, {'template_name': 'login.html'}, name='auth_login'),
    url(r'^accounts/logout/', auth.views.logout, {'template_name': 'logout.html'}, name='auth_logout'),
    
    url(r'^chat/', include('chatrooms.urls')),
    
    
    # Apps
    #(r'^forum/account/', include('django_authopenid.urls')),
    (r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),

    url(r'^$' , views.home_page),
    url(r'^profile/$' , views.profile_page),
    url(r'^info/(?P<page_name>[\w-]+)/$' , views.info_page),
    
)


# PM Extension
if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^forum/pm/', include('django_messages.urls')),
   )