from django.contrib.auth.models import User
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *
# Create your views here.

def user_signup(request):

    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            user=User.objects.create_user(username=username,email=email,password=pass1)
            user.save()
            return redirect('login')
        
    return render (request,'signup.html')


def user_login(request):
    
    if request.user.is_authenticated:
        return redirect('index')
   
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            # return redirect('index')
            return JsonResponse({
                'success': True,
            },safe=False)

        # return HttpResponse("Invalid Credentials!!")
        return JsonResponse({
            'success': False,
        },safe=False)

    return render(request,'login.html')


@login_required(login_url = 'login')
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
        
    contexts = {
        "tasks":tasks,
        "form": form
    }
    return render(request,'index.html',contexts)


@login_required(login_url = 'login')
def update_task(request,pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect(index)

    contexts = {
        "tasks":tasks,
        "form": form
    }

    return render(request,'update_task.html',contexts)

@login_required(login_url = 'login')
def delete_task(request,pk):
    
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
            item.delete()
            return redirect(index)
    
    contexts = {
        "item": item
    }
    
    return render(request,'delete.html',contexts)

@login_required(login_url ='login')
def user_logout(request):
    logout(request)
    return redirect('/')

