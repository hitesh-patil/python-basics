from django.http import HttpResponse
from django.shortcuts import render

def about(request):
  return HttpResponse("About page")

def home(request):
  # return HttpResponse("home page")
  return render(request,"homepage.html")