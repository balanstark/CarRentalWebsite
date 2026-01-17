from django.shortcuts import render,redirect
from userformapp.forms import UserForm,UserProfileForm,UserUpdateForm,UserProfileUpdateForm,PasswordResetForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def registration(request):
    registered = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        form1 = UserProfileForm(request.POST,request.FILES)

        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
    else:
        form = UserForm()
        form1 = UserProfileForm()
    context = {
        'form':form,
        'form1':form1,
        'registered': registered
    }
    return render(request,'registration.html',context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('User is not active ! please register again...')
        else:
            return HttpResponse("Please check your credentials...")
    return render(request,'login.html',{})

@login_required(login_url = 'login')
def home(request):
    return render(request,'home.html',{})

@login_required(login_url = 'login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
def profile(request):
    return render(request,'profile.html',{})

@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance=request.user)
        form1 = UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.userdetails)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.save()

            profile = form1.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
        form1 = UserProfileUpdateForm(instance=request.user.userdetails)

    context = {
        "form":form,
        'form1':form1
    }
    return render(request,'update.html',context)

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            new_password = form.cleaned_data['new_password']
            try:
                user = User.objects.get(username = username)
                user.set_password(new_password)
                user.save()
            except :
                return HttpResponse('User does not exist')
    else:
        form = PasswordResetForm()

    context = {
        'form':form
    }
    return render(request,'password_reset.html',context)
