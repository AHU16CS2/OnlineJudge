from django.urls import path
from . import views

app_name = 'problem'
urlpatterns = [
    path('problist/', views.problist, name='题目列表'),
]
