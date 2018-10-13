from django.urls import path
from . import views



app_name = 'account'
urlpatterns = [
    path('ranklist/', views.ranklist, name='排名'),
]
