from django.shortcuts import render,redirect,get_object_or_404
from .models import *
import random


color_list=('danger',
            'success',
            'info',
            'primary',
            'warning',
            )


default_gif_list=  ('default1.gif',
                    'default2.gif',
                    'default3.gif',
                    'default4.gif',
                    'default5.gif',
                    )



def index(request):  #新闻列表
    rows1 = list(new.objects.all())
    rows2 = list(motto.objects.all())
    random.shuffle(rows2)
    ans=[];j=0
    jiange=3
    for i in range(len(rows1)):  
        ans.append(rows1[i])
        if (i+1)% jiange==0 and j<len(rows2):
            ans.append(rows2[j])
            j=j+1
    Dict = {'新闻们' : ans,'名言的颜色们' : color_list,'新闻们的默认图片':default_gif_list}
    return render(request,'oj_base/index.html',Dict)



def about(request):
    return render(request, 'oj_base/about.html')



def news_detail(request, 每个新闻_id):
    try:
        row = new.objects.get(id=每个新闻_id)  # 唯一
    except new.DoesNotExist:
        return render(request, 'oj_base/alert/not_exist.html')
    Dict = { 'news_detail'  : row}
    return render(request, 'oj_base/news_detail.html',Dict)



def edit_new(request, 每个新闻_id):
    if request.method == "POST":
        pass
        # s=request.POST['已修改事项']
        # if s == '':
        #     return render(request,'oj_base/edit_news.html',{'警告':'请输入内容！'})  
        # else:
        #     row=Todo.objects.get(id=每个新闻_id)
        #     row.thing=s
        #     row.save()
        #     return redirect('todolist:主页')
    elif request.method == "GET":
        # row=Todo.objects.get(id=每个新闻_id)
        # content = { '待修改事项'  : row.thing}  #显示之前已经有的东西
        return render(request,'oj_base/edit_new.html')
    else:
        pass