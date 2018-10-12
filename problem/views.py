from django.shortcuts import render

# Create your views here.

def problist(request):
    return render(request, 'problem/problist.html')
