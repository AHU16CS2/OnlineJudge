from django.urls import path
from . import views
from . import models
app_name = 'problem'
urlpatterns = [
    path('problist/', views.problist, name='题目列表'),
    path('problem/<int:Pid>/',views.problem_page,name='题目描述'),
    #path('problem/'+'1002',views.problem,name='题目描述2'),
]
