from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('my/', views.my_tasks, name='my_tasks'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('create/', views.task_create, name='task_create'),
    path('<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('<int:task_id>/status/', views.task_update_status, name='task_update_status'),
    path('<int:task_id>/evaluate/', views.task_evaluate, name='task_evaluate'),
]