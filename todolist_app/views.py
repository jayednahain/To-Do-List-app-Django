from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.



def index_function(request):

   context ={
      'welcome_text': "Welcome to the home page",
      'title_heading': "Home page",
   }

   return render(request, 'index.html', context)







def todolist_function(request):


   if request.method == "POST":
      form = TaskForm(request.POST or None)
      if form.is_valid():
         form.save()

      # alert message
      message_text = "New task added successfully"
      messages.success(request, (message_text))

      return redirect('todolist_link')
   else:
      all_task = TaskList.objects.all()
      '''value_limit_per_page = 5
      paginator = Paginator(all_task,value_limit_per_page)
      page= request.GET.get('pg')
      all_task=paginator.get_page(page)'''

      context = {
         'welcome_text': "welcome to todo list page",
         'title_heading': "todo list",
         'all_task': all_task
      }
      return render(request, 'todolist_app.html', context)


def delete_task(request, task_id):
   task = TaskList.objects.get(pk=task_id)
   if task.delete():
      message_text_delete = "delete successfully"
      messages.success(request, (message_text_delete))

   return redirect('todolist_link')




def edit_task(request, task_id):
   if request.method == "POST":
      task = TaskList.objects.get(pk=task_id)
      form = TaskForm(request.POST or None,instance=task)
      if form.is_valid():
         form.save()

      massage_text = "Task Edited Successfully"
      messages.success(request, (massage_text))

      return redirect('todolist_link')
   else:
      edit_object = TaskList.objects.get(pk=task_id)
      context = {
         'welcome_text': "This is edit section",
         'title_heading': "Edit list",
         'edit_object': edit_object
      }

      return render(request, 'edit.html', context)

def complete_task(request,task_id):
   task = TaskList.objects.get(pk=task_id)
   task.done = True
   task.save()

   return redirect('todolist_link')

def pending_task(request,task_id):
   task = TaskList.objects.get(pk=task_id)
   task.done = False
   task.save()

   return redirect('todolist_link')



def about_section(request):
   return render(request,'about_section.html')
