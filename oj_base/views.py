import datetime
import random,math
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import *


color_list=('danger',
            'success',
            'info',
            'primary',
            'warning',
            )


# default_gif_list=  ('default1.gif',
#                     'default2.gif',
#                     'default3.gif',
#                     'default4.gif',
#                     'default5.gif',
#                     )
default_gif_list=('ahu2.png',)


def yuming(request):
    return redirect('/index?type=0&page=1')


def index(request):
    if request.method =="POST":
        tmp_type=request.POST['当前分类']
        tmp_page=request.POST['跳转至页数']
        return redirect("/index?type={}&page={}".format(tmp_type,tmp_page))
    page_capacity = 4  # 每页展示的新闻数量
    newstype = request.GET.get('type')
    page = request.GET.get('page')
    if page == None :
        page = 1
    else:
        page =int(page)
    if newstype == None :
        newstype = 0
    else:
        newstype =int(newstype)

    if newstype==0:
        rows1 = list(new.objects.filter(is_deleted=False)) 
    else:
        row = get_object_or_404(newsType,pk=newstype)
        rows1 = list(new.objects.filter(is_deleted=False, newstype=row))
    news_num = len(rows1) # 当前类别的新闻数量
    page_num = math.ceil(news_num/page_capacity)  # 当前类别的新闻页数
    if page_num!=0 and (page > page_num or page < 1 ) :
        return render(request,"oj_base/alert/not_exist.html") 
    if page == page_num:
        rows1 = rows1[page_capacity*(page-1) : ]
    else:
        rows1 = rows1[page_capacity*(page-1) : page_capacity*page]
    rows2 = list(motto.objects.filter(is_deleted=False))
    rows3 = list(newsType.objects.all())
    random.shuffle(rows2)  # 打乱名言的显示顺序
    ans=[];j=0
    jiange=3  # 每多少篇新闻加入一句名言
    for i in range(len(rows1)):  
        ans.append(rows1[i])
        if (i+1)% jiange==0 and len(rows2):
            ans.append(rows2[j])
            j=j+1
            if j==len(rows2):
                j=0
    Dict = {'新闻们' : ans,
            '颜色们' : color_list,
            '新闻们的默认图片':default_gif_list,
            '新闻总数':news_num,
            '当前页数':page,
            '总页数':page_num,
            '新闻类别们':rows3,
            '当前分类':newstype
            }
    return render(request,'oj_base/index.html',Dict)



def news_detail(request, 每个新闻_id):
    try:
        row = new.objects.get(id=每个新闻_id)  # 唯一
    except new.DoesNotExist:
        return render(request, 'oj_base/alert/not_exist.html')
    Dict = { 'news_detail'  : row }
    return render(request, 'oj_base/news_detail.html', Dict)


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



def about(request):
    return render(request, 'oj_base/about.html')


