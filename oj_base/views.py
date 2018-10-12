from django.shortcuts import render,redirect
# from .models import 


# Create your views here.
def index(request):
    return render(request,'oj_base/index.html')

def about(request):
    return render(request, 'oj_base/about.html')

