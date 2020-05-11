from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *


def index(request):
    return HttpResponse("Hello, world. You're at the test index.")


def main(request):
    if request.user.is_authenticated:
        Courses = Course.objects.all()
        user = request.user
        return render(request, 'mysite/main.html', {"Courses": Courses, "user": user})
    else:
        return HttpResponseRedirect('login/')


def course(request, course_id):
    crs = Course.objects.get(pk=course_id)
    books = Course_book.objects.filter(course_id_id = course_id)
    user = request.user
    return render(request, 'mysite/course.html', {"сourse": crs, 'books': books, "user": user})


def courses(request):
    crss = Course.objects.all()
    user = request.user
    return render(request, 'mysite/courses.html', {'courses': crss, "user": user})
