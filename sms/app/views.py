from django.shortcuts import render
from django.http import HttpResponse
# def home(request):
#     return HttpResponse('home page')
# def about(request): #http://127.0.0.1:8000/
#     return HttpResponse('About page')
# def student(request):
#     return HttpResponse('Student Page')
# def contact(request):
#     return HttpResponse('Contact Page')
# def services(request):
#     return HttpResponse('Service Page')

def home(request):
    return render(request,template_name = 'index.html')

def about(request):
    return render(request,'about.html')