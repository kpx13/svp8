# -*- coding: utf-8 -*-

import datetime
from django.core.context_processors import csrf
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import auth
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from pages.models import Page
from subscribe.models import Subscribe
from django.contrib.auth.decorators import login_required
from chatrooms.models import Room, Message

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['username'] = request.user.username
    c['info_pages'] = Page.objects.all()
    c.update(csrf(request))
        
    return c

@login_required
def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['room'] = Room.objects.all()[0]
    c['chat_messages'] = Message.objects.filter(room=c['room'])
    c['content'] = Page.get_page_by_slug('home')['content']
    return render_to_response('home.html', c, context_instance=RequestContext(request))

@login_required
def profile_page(request):
    c = get_common_context(request)
    c['user'] = request.user
    
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            print '&&&'
            messages.success(request, u'Ваш пароль успешно изменен')
            return HttpResponseRedirect('/profile')
        else:
            print form
            c['password_form'] = form
    else:
        c['password_form'] = PasswordChangeForm(request.user)
    return render_to_response('profile.html', c, context_instance=RequestContext(request))

@login_required
def info_page(request, page_name):
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
