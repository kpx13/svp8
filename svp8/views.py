# -*- coding: utf-8 -*-

import datetime
from django.core.context_processors import csrf
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from pages.models import Page
from subscribe.models import Subscribe

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c.update(csrf(request))
    
    if request.method == "POST":
        Subscribe(email=request.POST.get('email'),
                  from_page=request.POST.get('from')).save()
        messages.success(request, u'Мы с Вами свяжемся. Спасибо за проявленный интерес.')
        
    return c

def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def other_page(request, page_name):
    c = get_common_context(request)
    try:
        c.update(Page.get_page_by_slug(page_name))
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    except:
        raise Http404()
