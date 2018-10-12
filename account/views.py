from django.shortcuts import render

# Create your views here.

def ranklist(request):
    return render(request, 'account/ranklist.html')
