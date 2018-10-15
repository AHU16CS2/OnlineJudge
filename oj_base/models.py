from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User



class newsType(models.Model):  # 新闻的类型 一对一
    type_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.type_name

class new(models.Model):
    title = models.CharField(max_length=60)
    newstype = models.ForeignKey(newsType, on_delete=models.DO_NOTHING)  #由于newsType __str__返回type_name  但实际上存的是newsType的一整个对象
    author = models.ForeignKey(User, on_delete = models.DO_NOTHING, default="1")  #删除作者时，不删除文章  只有1个超级管理员   
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)  # 更新时会自动更改
    is_deleted = models.BooleanField(default=False)  # 可以理解为划掉操作 没有真正的删除 起到一个缓冲的作用 避免数据丢失

    def __str__(self):
        return "<new: %s>" % self.title





class motto(models.Model):
    mottoauthor = models.CharField(max_length=30)
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)  # 可以理解为划掉操作 没有真正的删除 起到一个缓冲的作用 避免数据丢失
    
    
    def __str__(self):
        return "<motto: %s>" % self.mottoauthor