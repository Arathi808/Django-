from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Student, Course
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

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
    students = Student.objects.all()
    total = students.count()
    passed = students.filter(mark__gte=35).count()
    average = students.aggregate(avg=Avg('mark'))['avg'] or 0
    print(request.user.is_authenticated)
    context = {
        'total_students': total,
        'total_courses':Course.objects.count(),
        'average_mark': round(average),
        'pass_rate':round(passed/total *100) if total else 0,
        'top_students': students.order_by('-mark')[:3],
        'recent_students':students.order_by('-id')[:5],
        'is_logged_in':request.user.is_authenticated
    }
    return render(request, 'index.html',context)

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
    return render(request, 'students.html', {'students':all_students, 'courses':courses,'is_logged_in':request.user.is_authenticated})

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

@login_required
def get_student(request,id):
    student = Student.objects.get(id=id)
    return render(request,'student.html',{'student':student})

@login_required
def add_student(request):
    if request.method == 'POST':
        image=request.FILES.get('profile')
        name=request.POST['name']
        age=int(request.POST['age'])
        mark=int(request.POST['mark'])
        course_id = request.POST['course']
        course=get_object_or_404(Course,id=course_id)
        print(course)
        Student.objects.create(name=name, age=age, mark=mark, course=course,image=image)
        return redirect('view_students')
    courses = Course.objects.all()
    return render(request,'add_student.html',{'courses':courses})

@login_required
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

@login_required
def delete_student(request,id):
    student = Student.objects.get(id=id)
    # print(student)
    student.delete()

    return redirect('view_students')