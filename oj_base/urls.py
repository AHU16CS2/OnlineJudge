from django.urls import path
from . import views

app_name = 'oj_base'
urlpatterns = [
    path('', views.index,name='主页'),
    path('about/', views.about, name='关于'),
    path('news/<int:每个新闻_id>',views.news_detail, name='新闻'),
    path('news/edit/<int:每个新闻_id>',views.edit_new, name='编辑新闻'),
    # path('del/<每一件事_id>', views.delete, name='删除'),
    # path('cross/<每一件事_id>', views.cross, name='划掉')
]
