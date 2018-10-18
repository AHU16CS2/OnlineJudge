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
from .models import Profile
from .forms import LoginForm, RegForm, InfoForm


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



def change_user_info(request):
    if request.method == 'POST':
        info_form = InfoForm(request.POST)
        if info_form.is_valid():
            nickname_new = info_form.cleaned_data['nickname']
            motto = info_form.cleaned_data['Motto']
            gender = info_form.cleaned_data['Gender']
            nation = info_form.cleaned_data['Nation']
            profile, created = Profile.objects.get_or_create(user=request.user)#注意这个坑，只用get会出现Profile matching query does not exist.错误
            profile.nickname = nickname_new
            profile.Gender = gender
            profile.Nation = nation
            profile.Motto = motto
            profile.save()
            return redirect('..')
        else :
            pass
    else:
        info_form =InfoForm()
    context = {}
    context['info_form'] = info_form
    return render(request, 'account/change_user_info.html',context)

