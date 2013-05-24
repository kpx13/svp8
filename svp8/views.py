# -*- coding: utf-8 -*-

import datetime
from django.core.context_processors import csrf
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import auth
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from pages.models import Page
from subscribe.models import Subscribe
from django.contrib.auth.decorators import login_required
from chatrooms.models import Room

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c.update(csrf(request))
    
    if request.method == "POST":
        Subscribe(email=request.POST.get('email'),
                  from_page=request.POST.get('from')).save()
        messages.success(request, u'Мы с Вами свяжемся. Спасибо за проявленный интерес.')
        
    return c

@login_required
def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['room'] = Room.objects.all()[0]
    return render_to_response('home.html', c, context_instance=RequestContext(request))

@login_required
def go_page(request):
    c = get_common_context(request)
    return render_to_response('go.html', c, context_instance=RequestContext(request))

@login_required
def play_page(request):
    c = get_common_context(request)
    return render_to_response('play.html', c, context_instance=RequestContext(request))

@login_required
def other_page(request, page_name):
    c = get_common_context(request)
    try:
        c.update(Page.get_page_by_slug(page_name))
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    except:
        raise Http404()
    
def login_user(request, c):
    form = AuthenticationForm(request.POST)
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            messages.success(request, u'Вы успешно вошли на сайт.')
            return True
        else:
            c['authentication_form'] = form
            messages.error(request, u'Ваш аккаунт не активирован.')
            return False
    else:
        c['authentication_form'] = form
        messages.error(request, u'Неверный логин или пароль.')
        return False
    return HttpResponseRedirect('/')


def logout_user(request):
    auth.logout(request)
