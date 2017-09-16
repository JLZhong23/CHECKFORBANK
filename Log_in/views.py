# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

#from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from forms import LoginForm
from django.shortcuts import render


def login_test(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html', {'form':form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render(request,'name.html', {'form':form})
            else:
                return render(request,'login.html', {'form':form})
        else:
            return render(request,'login.html', {'form':form})


def login(request):
    return render_to_response("login.html")

def regist(request):
    return render_to_response("regist.html")
