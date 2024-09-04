from django.urls import path
from .views import task_list, task_details, add_task, delete_task, update_task, add_task_form, update_task_form

urlpatterns = [
    path('alltasks/', task_list, name="task_list"),
    path('alltasks/<int:pk>/', task_details, name="task_details"),
    path('addtask/', add_task, name="add_task"),
    path('deletetask/<int:pk>/', delete_task, name="delete_task"),
    path('updatetask/<int:pk>/', update_task, name="update_task"),
    path('addtaskform/', add_task_form, name="add_task_form"),
    path('updatetaskform/<int:pk>/', update_task_form, name="update_task_form"),

]
