from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
import sys
# sys.path.append("D:\Online Judge of AHU\OnlineJudge\problem")
from problem.models import Problems


class Status(models.Model):
    Status_ID = models.AutoField(primary_key=True)
    Submit_Time = models.DateTimeField(verbose_name="提交时间")
    Judge_Status = models.CharField(max_length=20, verbose_name="评测状态")
    Prob_ID = models.ForeignKey(Problems, on_delete=models.DO_NOTHING)  # 与Problem表关联
    Exe_Time = models.CharField(max_length=10, verbose_name="执行时间")
    Exe_Memory = models.CharField(max_length=10, verbose_name="执行内存")
    Code_Len = models.CharField(max_length=10, verbose_name="代码长度")
    Language = models.CharField(max_length=10, verbose_name="代码语言")
    Author = models.OneToOneField(User, on_delete=models.DO_NOTHING)  # 与User表关联

    def __str__(self):
        return '<Status: %s for %s>' % (self.Status_ID, self.Author.nickname)
