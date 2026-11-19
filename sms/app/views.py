from django.shortcuts import render,redirect,get_object_or_404
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
    search = request.GET.get('search')
    if course:
        all_students = Student.objects.filter(course=course)  
    else:
        all_students = Student.objects.all()
    if search:
        all_students = Student.objects.filter(name__icontains=search)  
    courses = Course.objects.all()
    return render(request, 'students.html', {'students':all_students, 'courses':courses})

# def students(request):
#     course=request.GET.get('course')
#     if course:
#        all_students=Student.objects.filter(course=course)
#     else:   
#         all_students=Student.objects.all()
#     search = request.GET.get('search')

#     if search:
#         all_students = all_students.filter(name__icontains=search)
#     courses=Course.objects.all()
#     return render(request,'students.html',{'students':all_students,'courses':courses})

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
        course_id = request.POST['course']
        course=get_object_or_404(Course,id=course_id)
        print(course)
        Student.objects.create(name=name, age=age, mark=mark, course=course)
        return redirect('view_students')
    courses = Course.objects.all()
    return render(request,'add_student.html',{'courses':courses})

def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = int(request.POST['age'])
        student.mark = int(request.POST['mark'])
        student.course = get_object_or_404(Course,id=request.POST['course'])
        student.save()
        return redirect('view_students')
    courses=Course.objects.all()
    return render(request,'edit.html',{'student':student,'courses':courses})

def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('view_students')