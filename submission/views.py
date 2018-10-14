from django.shortcuts import render

# Create your views here.

def status(request):
    return render(request, 'submission/status.html')
