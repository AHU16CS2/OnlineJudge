from django.urls import path
from . import views



app_name = 'account'
urlpatterns = [
    path('ranklist/', views.ranklist, name='排名'),
    path('user_info/', views.user_info, name='user_info'),
    path('login/',views.login,name='登录'),
    path('register/',views.register,name='注册'),
    path('logout/',views.logout,name='登出'),
]
