from django.db import models
import sys
sys.path.append("..")
from problem.models import Problems
# Create your models here.


#【密】用户账号信息，用于后台管理，不显示给用户
class Users(models.Model):
    Id = models.AutoField(primary_key=True)                 #用户编号，主键
    Name=models.CharField(max_length=20,null=False)         #用户名
    Password=models.CharField(max_length=25,null=False)     #用户密码
    Reg_Email=models.TextField(null=False)                  #用户注册邮箱
    Reg_Time=models.DateField()                             #用户注册日期


#用户个人扩展信息，可显示给用户
class Users_Info(models.Model):
    Id=models.OneToOneField(Users,on_delete=models.CASCADE) #用户信息编号，与Users的主键ID对应
    Name=models.CharField(max_length=20,null=False)         #用户名
    Gender=models.CharField(max_length=5,null=True)         #用户性别
    Nation=models.CharField(max_length=15,null=True)        #国籍
    Motto=models.TextField(null=True)                       #个人签名
    Submit_num=models.IntegerField()                        #提交总次数
    Ac_num=models.IntegerField()                            #AC题数
    #All_problems=models.ManyToManyField(Problems)           #用户与题目之间为多对多关系
    ##需要标记题目为AC或者未AC
    #user_type_choices = (
    #    (1, 'superuser'),
    #   (2, 'commonuser'),
    #)
    #user_type_id = models.IntegerField(choices=user_type_choices, default=1)
###


