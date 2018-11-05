from django.urls import path
from . import views

app_name = 'submission'
urlpatterns = [
    path('status/<int:每个评测_id>', views.status_page, name='评测状态'),
    path('statuslist/',views.statuslist,name='评测记录')
]
