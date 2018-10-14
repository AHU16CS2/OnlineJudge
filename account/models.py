#models.py
import sys
sys.path.append("..")
from problem.models import Problems
# models.py

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
#import sys
#sys.path.append("..")
#from problem.models import Problems

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, Gender,Nation,Motto,Reg_Time,Submit_num,Ac_num,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            Gender=Gender,
            Nation=Nation,
            Motto=Motto,
            Reg_Time=Reg_Time,
            Submit_num=Submit_num,
            Ac_num=Ac_num,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, Gender,Nation,Motto,Reg_Time,Submit_num,Ac_num,password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth,
            Gender=Gender,
            Nation=Nation,
            Motto=Motto,
            Reg_Time=Reg_Time,
            Submit_num=Submit_num,
            Ac_num=Ac_num
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    Gender = models.CharField(max_length=5, null=True)  # 用户性别
    Nation = models.CharField(max_length=15, null=True)  # 国籍
    Motto = models.TextField(null=True)  # 个人签名
    Reg_Time=models.DateField(null=True)          #用户注册日期
    Submit_num = models.IntegerField(default=0)  # 提交总次数
    Ac_num = models.IntegerField(default=0)  # AC题数
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'Gender','Nation','Motto','Reg_Time','Submit_num','Ac_num']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    #All_problems=models.ManyToManyField(Problems)           #用户与题目之间为多对多关系
    ##需要标记题目为AC或者未AC


