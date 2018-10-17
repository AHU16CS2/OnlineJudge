import  datetime
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
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



def index(request):  #总新闻列表 
    # 分页处理还没写
    rows1 = list(new.objects.filter(is_deleted=False))  #注意get与filter的区别
    rows2 = list(motto.objects.filter(is_deleted=False))
    rows3 = list(newsType.objects.all())
    random.shuffle(rows2)  # 打乱名言的显示顺序
    ans=[];j=0
    jiange=3  # 每多少篇新闻加入一句名言
    for i in range(len(rows1)):  
        ans.append(rows1[i])
        if (i+1)% jiange==0:
            ans.append(rows2[j])
            j=j+1
            if j==len(rows2):
                j=0
    Dict = {'新闻们' : ans,'颜色们' : color_list,'新闻们的默认图片':default_gif_list,
           '新闻总数':len(rows1),'新闻类别们':rows3,'所有分类高亮':'active'}
    return render(request,'oj_base/index.html',Dict)



def news_with_type(request, 新闻种类_id):  # 过滤新闻种类 
    row = get_object_or_404(newsType,pk=新闻种类_id)  #print(new_type)
    rows1 = list(new.objects.filter(is_deleted=False, newstype=row))  #注意get与filter的区别  
    rows2 = list(motto.objects.filter(is_deleted=False))
    rows3 = list(newsType.objects.all())
    random.shuffle(rows2)  # 打乱名言的显示顺序
    ans=[];j=0
    jiange=3  # 每多少篇新闻加入一句名言
    for i in range(len(rows1)):  
        ans.append(rows1[i])
        if (i+1)% jiange==0:
            ans.append(rows2[j])
            j=j+1
            if j==len(rows2):
                j=0
    # print(type(row))
    # print(type(rows3[0]))
    Dict = {'新闻们' : ans,'颜色们' : color_list,'新闻们的默认图片':default_gif_list,
           '新闻总数':len(rows1),'新闻类别们':rows3,'当前分类':row.id}
    return render(request,'oj_base/index.html',Dict)



def news_detail(request, 每个新闻_id):
    try:
        row = new.objects.get(id=每个新闻_id)  # 唯一
    except new.DoesNotExist:
        return render(request, 'oj_base/alert/not_exist.html')
    Dict = { 'news_detail'  : row }
    return render(request, 'oj_base/news_detail.html', Dict)



def edit_new(request, 每个新闻_id):  # 跳转后后台管理
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



def about(request):
    return render(request, 'oj_base/about.html')


