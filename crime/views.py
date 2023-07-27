from django.shortcuts import render
from django.http import HttpResponse

def say(request):
    return HttpResponse("hello")

def render_page(request):
    return render(request, "test.html")