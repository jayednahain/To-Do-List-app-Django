from django.urls import path,include
from book_lesson_app import views

urlpatterns = [
    path('',views.welcome_function,name='welcome_link'),
    path('lesson_one',views.lesson_one_function,name='lesson_one_link'),
    path('lesson_two',views.lesson_two_function,name='lesson_two_link'),
    path('lesson_three',views.lesson_three_function,name='lesson_three_link'),
    path('lesson_four',views.lesson_four_function,name='lesson_four_link'),

]
