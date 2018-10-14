from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *
from django.contrib import auth
from django import forms  # 导入表单
#from django.contrib.auth.models import User  # 导入自定义表

from django.shortcuts import render, redirect


def user_info(request):
    context = {}
    return render(request, 'account/user_info.html', context)

def ranklist(request):
    return render(request, 'account/ranklist.html')
