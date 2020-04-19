from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Hello, world. You're at the test index.")


def main(request):
    if request.user.is_authenticated:
        return render(request, 'mysite/main.html')
    else:
        return HttpResponseRedirect('login/')
