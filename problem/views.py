from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import HttpResponseRedirect
import math,random
from .models import *
from submission.models import *

# Create your views here.

def tianjia(times):
    for i in range(0,times):
        a=random.randint(0,20000)
        b=random.randint(0,a)
        new_row=Problems(   Headline="test"+str(i),
                            Time_Limit=1000,Memory_Limit=64,
                            Prob_Description="test",
                            Input="test",
                            Output="test",
                            Total_submision=a,
                            Total_AC=b,
                        )
        new_row.save()
        new_row.Tags.set(str(random.randint(1,3)))

def problist(request):
    #tianjia(5000)
    if request.method =="POST":
        tmp_type=request.POST['当前分类']
        tmp_page=request.POST['跳转至页数']
        # 这里要判断一下非数字的情况
        return redirect("/problist?type={}&page={}".format(tmp_type,tmp_page))
    page_capacity = 50  # 每页展示的题目数量  可以提供几个选项 20 50 100
    problemtag = request.GET.get('type')
    page = request.GET.get('page')
    if page == None :
        page = 1
    else:
        page =int(page)
    if problemtag == None :
        problemtag = 0
    else:
        problemtag =int(problemtag)

    if problemtag==0:
        rows1 = list(Problems.objects.filter(is_deleted=False)) 
    else:
        rows1 = Problems.objects.filter(Tags=problemtag)
    prob_num = len(rows1) # 当前类别的题目数量
    page_num = math.ceil(prob_num/page_capacity)  # 当前类别的新闻页数
    if page_num!=0 and (page > page_num or page < 1 ) :
        return render(request,"oj_base/alert/not_exist.html") 
    if page == page_num:
        rows1 = rows1[page_capacity*(page-1) : ]
    else:
        rows1 = rows1[page_capacity*(page-1) : page_capacity*page]
    rows3 = list(Tag.objects.all())

    taglist=[] #每个题目对应的标签
    for item in rows1:
        taglist.append(list(item.Tags.values()))

    Dict = {
            '题目总数':prob_num,
            '当前页数':page,
            '总页数':page_num,
            'problems': rows1,
            '题目类别们':rows3,
            '当前分类':problemtag,
            '标签们':taglist,
            }
    return render(request,'problem/problist.html',Dict)

def submit(request):    # 提交代码时的函数
    author = str(request.user.username)
    code = request.POST.get('code')
    # print(code)
    id = int(request.POST.get('id'))
    language = request.POST.getlist('language') # 取得的是list
    language = ''.join(language)
    new_row=Status(     
                        Judge_Status="Pending",
                        Compile_Error_Info="None",
                        Prob_ID=Problems.objects.get(pk=id),
                        Exe_Time='0',
                        Exe_Memory='0',
                        Code_Len=len(code),
                        Language=language,
                        Author=User.objects.get(username=author),
                        Code=code,
                )
    new_row.save()
    return HttpResponseRedirect('/statuslist/')
    # return HttpResponseRedirect('/status/id?')问题在于得到评测的id号

def problem_page(request,每个题目_id):
    problem = Problems.objects.get(pk=每个题目_id)
    tag=list(problem.Tags.values())
    Dict={
        'problem': problem,
        '标签':tag,
    }
    return render(request, 'problem/problem.html', Dict)
