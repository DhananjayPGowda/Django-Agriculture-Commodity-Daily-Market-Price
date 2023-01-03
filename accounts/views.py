from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def Login(request):
    if request.method == "GET":
        return render(request,'login.html')
        
          
    un = request.POST['username']
    pw = request.POST['password']
    user = authenticate(request,username = un, password = pw)
    if user is not None:
        l = login(request,user)
        print("logged in ",user)
    else:
        messages.info(request,'userid and password not matching')
        return redirect('/accounts/login')
    return redirect('/')

    
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    r = request.POST

    if r['password1'] == r['password2']:
        if not User.objects.filter(username = r['username']).exists():
            if not User.objects.filter(email = r['email']).exists():
                user = User.objects.create_user(first_name = r['firstname'],last_name = r['lastname'],email = r['email'],username=r['username'],password=r['password1'])
                if user is not None:
                    user.save()
                    print('user created')
                    return redirect('/accounts/login')
            else:
                messages.info(request,'email already exists')
                
        else:
            messages.info(request,'username already exists')
    else:
        messages.info(request,'password1 and password2 not matching')
    return redirect('/accounts/signup')
    
    
def Logout(request):    
    logout(request)
    return redirect('/')
    
