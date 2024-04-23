from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
# Create your views here.
def HomePage(request):
     return render(request,'home.html')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if(pass1!=pass2):
            return HttpResponse('your password is not same ')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return  redirect('login')
    # HttpResponse("User has created Successfully")
        # print(uname,email,pass1,pass2)
    return render(request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        # print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('password is incorrect!!!')
        
def LogoutPage(request):
    logout(request)
    return redirect('login')
    
    # return render (request,'login.html') 