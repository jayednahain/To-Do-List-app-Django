from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def welcome_function(request):

   data = {
      "title":"Welcome",
      "heading":"Welcome to Book Lesson Page"
   }

   return render(request, 'book_lesson_app.html', data)


def lesson_one_function(request):
   data = {
      "title": "Lesson One",
      "heading": "Learn Jinga Syntex"
   }
   return render(request, 'lesson_one.html', data)


def lesson_two_function(request):
   data = {
      "title": "Lesson two",
      "heading": "Learn Filter function"
   }
   return render(request, 'lesson_two.html', data)


def lesson_three_function(request):
   data = {
      "title": "Lesson Four",
      "heading": "Looping jinga"
   }

   return render(request, 'lesson_three.html',data )


def lesson_four_function(request):
   data = {
      "title": "Lesson Four",
      "heading": "Nothing fo now"
   }

   return render(request, 'lesson_four.html',data )
