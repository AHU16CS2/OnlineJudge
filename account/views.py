from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *
from django.contrib import auth
from django import forms  # 导入表单
#from django.contrib.auth.models import User  # 导入自定义表


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密_码', widget=forms.PasswordInput())


# Django的form的作用：
# 1、生成html标签
# 2、用来做用户提交的验证
# Form的验证思路
# 前端：form表单
# 后台：创建form类，当请求到来时，先匹配，匹配出正确和错误信息。
def index(request):
    return render(request, 'index.html')


def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)  # 包含用户名和密码
        if uf.is_valid():
            # 获取表单数据
            username = uf.cleaned_data['username']  # cleaned_data类型是字典，里面是提交成功后的信息
            password = uf.cleaned_data['password']
            # 添加到数据库
            # registAdd = User.objects.get_or_create(username=username,password=password)
            registAdd = User.objects.create_user(username=username, password=password)
            # print registAdd
            if registAdd == False:
                return render(request, 'share1.html', {'registAdd': registAdd, 'username': username})

            else:
                # return HttpResponse('ok')
                return render(request, 'share1.html', {'registAdd': registAdd})
                # return render_to_response('share.html',{'registAdd':registAdd},context_instance = RequestContext(request))
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        uf = UserForm()
    # return render_to_response('regist.html',{'uf':uf},context_instance = RequestContext(request))
    return render(request, 'regist1.html', {'uf': uf})



# Create your views here.

def ranklist(request):
    return render(request, 'account/ranklist.html')
