from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from shop import models
from account.forms import RegForm, LogForm, PwdChangeForm


def register(request):  # register function
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            User.objects.create_user(username=username, password=password)
            return redirect('login')
    return render(request, 'account/register.html', {'form': form_obj})


def login(request):  # login function
    form_obj = LogForm()
    if request.method == "POST":
        form_obj = LogForm(request.POST)
        if form_obj.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(request, username=username, password=password)

            if user:
                auth.login(request, user)
                # path = request.GET.get('next') or 'http://127.0.0.1:8000'
                path = request.GET.get('next') or '/'
                return redirect(path)
            else:
                print('Username and password do not match')
                info = 'Username and password do not match'
                context = {'form': form_obj, 'info': info}
                return render(request, 'account/login.html', context=context)
    return render(request, 'account/login.html', context={'form': form_obj})


# @login_required(login_url='/login/')
# def index(request):
#     return render(request, 'index.html')


@login_required(login_url='/login/')
def logout(request):  # logout
    auth.logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def changePassword(request):  # change password
    form_pwd = PwdChangeForm()
    if request.method == "POST":
        form_pwd = PwdChangeForm(request.POST)
        if form_pwd.is_valid():
            # form has already verified the new_password and confirm_password
            # so confirm_password dont need to get again to verified
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return redirect('login')
            else:
                info = 'The old password is wrong!!!'
                return render(request, 'account/changePassword.html', {'form': form_pwd, 'info': info})
        else:
            form = PwdChangeForm()
    return render(request, 'account/changePassword.html', {'form': form_pwd})
