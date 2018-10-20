from django import forms
from django.contrib import auth
from django.contrib.auth.models import  User
from .models import Profile
from .models import Genders,Nations



class LoginForm( forms.Form ):
    username=forms.CharField(label='用户名',
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    password=forms.CharField(label='密码',
                             widget=forms.PasswordInput(
                                 attrs={'class': 'form-control', 'placeholder': '请输入密码'}))

    def clean(self):
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        user=auth.authenticate(username=username,password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user']=user
        return self.cleaned_data




class RegForm(forms.Form):
    username = forms.CharField(label='用户名',
                               max_length=30,
                               min_length=3,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    email = forms.EmailField(label='邮箱',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control', 'placeholder': '请输入邮箱'}))
    password = forms.CharField(label='密码',
                               min_length=6,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    password_again = forms.CharField(label='请再次输入密码',
                                     min_length=6,
                                     widget=forms.PasswordInput(
                                         attrs={'class': 'form-control', 'placeholder': '请再次输入密码'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已存在')
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次输入的密码不一致')
        return password_again



class InfoForm(forms.Form):
    nickname = forms.CharField(label='昵称：',
                               max_length=20,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '请输入用户名(不超过20字节)'}))
    Gender = forms.ChoiceField(label='性别：',
                               choices=Genders
                               )
    Nation = forms.ChoiceField(label='国家：',
                               choices=Nations
                               )
    Motto =forms.CharField(label='个人签名：',
                               max_length=200,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '这个人很懒，什么都没写嘤嘤嘤┭┮﹏┭┮(不超过200字节)'}))


    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if Profile.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError('昵称名已存在')
        return nickname

