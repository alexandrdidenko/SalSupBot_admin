# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import auth
from django.template.context_processors import csrf


def logon_view(request):
    args = {}
    args.update(csrf(request))
    #username_sesion = ''
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # username_sesion = auth._get_user_session_key(request)
            return redirect('../')
        else:
            args['login_error'] = 'User does not exist'
            return render(None,'authorization/authorization.html', args)
    else:
        return render(None,'authorization/authorization.html', args)


def logout_view(request):
    auth.logout(request)
    return redirect("/")
