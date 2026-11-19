from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student, Course
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
    return render(request, 'index.html',{'std_name':'Akhil'})

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request, 'services.html')

def students(request):
    course = request.GET.get('course')
    if course:
        all_students = Student.objects.filter(course=course)
    else:
        all_students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'students.html', {'students':all_students, 'courses':courses})

def contacts(request):
    return render(request, 'contacts.html')

def get_student(request,id):
    student = Student.objects.get(id=id)
    return render(request,'student.html',{'student':student})

def add_student(request):
    if request.method == 'POST':
        name=request.POST['name']
        age=int(request.POST['age'])
        mark=int(request.POST['mark'])
        course=request.POST['course']
        Student.objects.create(name=name, age=age, mark=mark, course=course)
        
        return redirect('view_students')
    return render(request,'add_student.html')

def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = int(request.POST['age'])
        student.mark = int(request.POST['mark'])
        student.course = request.POST['course']
        student.save()
        return redirect('view_students')
    return render(request,'edit.html',{'student':student})

def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('view_students')