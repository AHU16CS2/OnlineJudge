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
from submission.models import Status
from account.models import Profile
import math,random

#User.last_login
def user_info(request,nickname):

    profile = Profile.objects.filter(nickname=nickname)
    print("len = ",len(profile))
    status = Status.objects.filter(Author=profile[0].id)
    print("-------Total---------",len(status))

    #这里应该加一个filter,判断提交中的AC数
    status_ac = Status.objects.filter(Author=profile[0].id).filter(Judge_Status="Accepted")
    print("-------AC---------", len(status_ac))
    profile[0].AC_num = len(status_ac)
    profile[0].Submit_num=len(status)

    status_prob = Status.objects.filter(Author=profile[0].id).values('Prob_ID').distinct()
    print("----------------", status_prob)
    print("-------Total_prob---------", len(status_prob))
    print("-------++++++---------", status_prob.values('Prob_ID'))
    profile[0].Submit_prob_num=len(status_prob)
    status_ac_prob = Status.objects.filter(Author=profile[0].id).filter(Judge_Status="Accepted").values('Prob_ID').distinct()
    print("-------Total_ac_prob---------", len(status_ac_prob))
    print("-------++++++---------", status_ac_prob.values('Prob_ID'))
    profile[0].AC_prob_num=len(status_ac_prob)

    profile[0].save()

    context={
             #"url_part":profile,
            "profile":profile[0],
            "status_prob": status_prob,
            "status_ac_prob":status_ac_prob,
         }
    print("-------Total_ac_prob---------", len(status_ac_prob)),
    return render(request, 'account/user_info.html', context)


def ranklist(request):
    if request.method == "POST":
        tmp_type = request.POST['当前分类']
        tmp_page = request.POST['跳转至页数']
        # 这里要判断一下非数字的情况
        return redirect("/ranklist?&page={}".format(tmp_page))
    page_capacity = 100  # 每页展示的用户数量  可以提供几个选项 20 50 100d:dd
    page = request.GET.get('page')
    if page == None:
        page = 1
    else:
        page = int(page)
    rows1 = list(Profile.objects.filter(nickname__isnull=False).order_by("-AC_prob_num"))
    User_num = len(rows1)  # 当前类别的题目数量
    page_num = math.ceil(User_num / page_capacity)  # 当前类别的新闻页数
    if page_num != 0 and (page > page_num or page < 1):
        return render(request, "oj_base/alert/not_exist.html")
    if page == page_num:
        rows1 = rows1[page_capacity * (page - 1):]
    else:
        rows1 = rows1[page_capacity * (page - 1): page_capacity * page]
    Dict = {
        '用户总数': User_num,
        '当前页数': page,
        '总页数': page_num,
        'Users': rows1,
    }
    return render(request, 'account/ranklist.html', Dict)


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
            #nickname_new=username
            #profile, created = Profile.objects.get_or_create( user==user)  # 注意这个坑，只用get会出现Profile matching query does not exist.错误
            #profile.nickname = nickname_new
            #profile.save()
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

