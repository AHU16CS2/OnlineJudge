from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django import forms  # 导入表单
from .models import *
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import LoginForm,RegForm


def user_info(request):
    context = {}
    return render(request, 'account/user_info.html', context)


def ranklist(request):
    return render(request, 'account/ranklist.html')


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request,user)
            return redirect('..')
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request,'account/login.html',context)



def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            #注册
            user=User.objects.create_user(username, email, password)
            user.save()
            #登录
            user=auth.authenticate(username=username,password=password)
            auth.login(request, user)
            return redirect('..')
        else :
            pass
    else:
        reg_form =RegForm()
    context = {}
    context['reg_form'] = reg_form
    return render(request, 'account/register.html' , context)


def logout(request):
    auth.logout(request)
    return redirect('..')