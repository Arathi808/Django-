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

name = 'Akhil'
all_students = [
    {'name':'Akhil', 'age':20, 'mark':80,'course':'MBA'},
    {'name':'Arun', 'age':20, 'mark':40,'course':'BCA'},
    {'name':'Karthik', 'age':21, 'mark':21,'course':'BBA'},
    {'name':'Jinu', 'age':22, 'mark':45,'course':'MBA'},
]
def home(request):
    return render(request, 'index.html',{'std_name':'Akhil'})

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request, 'services.html')

def students(request):
    return render(request, 'students.html', {'students':all_students})

def contacts(request):
    return render(request, 'contacts.html')

def get_student(request,name):
    std = None
    for student in all_students:
        if student['name'] == name:
            std = student
    return render(request,'student.html',{'name':name,'student':std})