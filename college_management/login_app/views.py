from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('n1')
        password = request.POST.get('p1')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/login_app/success/')
    return render(request, 'login.html')

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')




def success(request):
    return render(request,'success.html')

from .forms import SignupForm
from django.contrib.auth.models import User

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login_app/login/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def Resethome(request):
    return render(request,'ResetPassword.html')


def resetPassword(request):
    responseDic={}
    try:
        usern = request.POST['uname']
        recepient=request.POST['email']
        pwd=request.POST['password']
        #subject="Password reset"
        try:
            user=User.objects.get(username=usern)
            if user is not None:
                user.set_password(pwd)
                user.save()
                #send_mail(subject,message, EMAIL_HOST_USER, [recepient])
                responseDic["errmsg"]="Password Reset Successfully"
                return render(request,"registration/ResetPassword.html",responseDic)
        except Exception as e:
            print(e)
            responseDic["errmsg"]="Email doesnt exist"
            return render(request,"registration/ResetPassword.html",responseDic)
        
    except Exception as e:
        print(e)
        responseDic["errmsg"]="Failed to reset password"
        return render(request,"registration/ResetPassword.html",responseDic)
