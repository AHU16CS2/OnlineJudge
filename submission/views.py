from django.shortcuts import render
import math,random
from .models import Status
from .models import User
from problem.models import Problems
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse

# Create your views here.

# def status(request):
#     return render(request, 'submission/status.html')


def tianjia(times):
    for i in range(0,times):
        a=random.randint(0,20000)
        b=random.randint(0,a)
        new_row=Status(     #Status_ID=str(i),
                            #Submit_Time=,
                            Judge_Status="Accepted",
                            Compile_Error_Info="None",
                            Prob_ID=Problems.objects.get(pk=5),
                            Exe_Time=str(i),
                            Exe_Memory=str(i),
                            Code_Len=str(300+i),
                            Language="c++",
                            Author=User.objects.get(pk=1),
                            Code="******",



                        )
        new_row.save()
        #new_row.Tags.set(str(random.randint(1,3)))


def statuslist(request):
    #tianjia(5)
    if request.method == "POST":
        tmp_type = request.POST['当前分类']
        tmp_page = request.POST['跳转至页数']
        # 这里要判断一下非数字的情况
        return redirect("/statuslist?&page={}".format(tmp_page))
    page_capacity = 100  # 每页展示的题目数量  可以提供几个选项 20 50 100d:dd
    page = request.GET.get('page')
    if page == None:
        page = 1
    else:
        page = int(page)
    rows1 = list(Status.objects.filter().order_by("-Submit_Time"))
    prob_num = len(rows1)  # 当前类别的题目数量
    page_num = math.ceil(prob_num / page_capacity)  # 当前类别的新闻页数
    if page_num != 0 and (page > page_num or page < 1):
        return render(request, "oj_base/alert/not_exist.html")
    if page == page_num:
        rows1 = rows1[page_capacity * (page - 1):]
    else:
        rows1 = rows1[page_capacity * (page - 1): page_capacity * page]
    Dict = {
        '评测总数': prob_num,
        '当前页数': page,
        '总页数': page_num,
        'statuses': rows1,
    }
    return render(request,'submission/statuslist.html',Dict)


def status_page(request,每个评测_id):
    status = Status.objects.get(pk=每个评测_id)
    
    Dict={
        'status': status,
    }
    return render(request, 'submission/status.html', Dict)