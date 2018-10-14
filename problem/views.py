from django.shortcuts import render

from . import models

# Create your views here.


def problist(request):
    problems = models.Problems.objects.all()
    return render(request, 'problem/problist.html',{'problems':problems})


def problem_page(request,Pid):
    problem = models.Problems.objects.get(pk=Pid)
    return render(request, 'problem/problem.html', {'problem': problem})
