from django.urls import path
from . import views
from . import models

app_name = 'problem'

urlpatterns = [
    path('problist/', views.problist, name='题目列表'),
    path('problem/<int:每个题目_id>',views.problem_page,name='题目描述'),
    path('problem/submit',views.submit,name='代码提交')
]
