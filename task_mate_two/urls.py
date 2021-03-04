"""



"""
from django.contrib import admin
from django.urls import path,include
from todolist_app import views as todolist_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',todolist_view.index_function,name='index_function_link'),

    path('task/',include('todolist_app.urls')),
    path('booklesson/',include('book_lesson_app.urls'))



]
