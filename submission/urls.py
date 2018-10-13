from django.urls import path
from . import views

app_name = 'submission'
urlpatterns = [
    path('status/', views.status, name='评测记录'),
]
