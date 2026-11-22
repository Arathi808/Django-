from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']
        if password == cpassword:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            return redirect('login')
        else:
            return render(request,'accounts/register.html',{'error':'Passwords doesnot match'})
    return render(request,'accounts/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if not user:
            return render(request,'accounts/login.html',{'error':'Invalid credentials'})
        login(request,user)
        return redirect('view_students')
    return render(request,'accounts/login.html')

def logout_view(request):
    logout(request)
    return render(request,'accounts/logout.html')