from django.contrib import admin
from django.urls import path,include
from todolist_app import views

urlpatterns = [
    path('',views.index_function,name='index_function_link'),
    path('task/',views.todolist_function,name='todolist_link'),


    path('delete/<task_id>',views.delete_task, name ='delete_task_link'),
    path('edit/<task_id>',views.edit_task, name ='edit_task_link'),
    path('complete/<task_id>',views.complete_task, name ='complete_task_link'),

    path('pending/<task_id>', views.pending_task, name='pending_task_link'),
    path('about_section',views.about_section,name="about_section_link")



]
