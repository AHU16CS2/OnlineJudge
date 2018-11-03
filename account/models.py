from django.db import models
from django.contrib.auth.models import User

Genders = (
  ( '男','男'),
  ( '女','女'),
)
Nations = (
    ('中国','中国'),
    ('美国', '美国'),
    ('加拿大', '加拿大'),
    ('英国', '英国'),

)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, verbose_name='昵称')
    Gender = models.CharField(max_length=10, verbose_name='性别')
    Nation = models.CharField(max_length=30, verbose_name='国籍')
    Motto = models.TextField(verbose_name='个人签名')
    AC_num = models.IntegerField(default=0, verbose_name='通过次数')
    Submit_num = models.IntegerField(default=0, verbose_name='提交次数')
    AC_prob_num = models.IntegerField(default=0, verbose_name='通过题数')
    Submit_prob_num = models.IntegerField(default=0, verbose_name='提交题数')
    def __str__(self):
        return '<Profile: %s for %s>' % (self.nickname, self.user.username)
