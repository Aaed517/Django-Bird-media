from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

from django.contrib.auth import login as auth_login,authenticate, logout as auth_logout
from django.contrib.auth.models import User
from .models import Account
from django.contrib import messages

# Create your views here.
def logout(request):
    auth_logout(request)
    messages.success(request,'Başarıyla Çıkış Yaptınız')
    return redirect('/account/login')

def login(request):
    form = LoginForm(request.POST or None)
    context ={
        'form' : form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username = username,password = password)
        if user:
            auth_login(request, user)
            return redirect('/account/login')
        else:
            messages.warning(request, "Kullanıcı Adı veya Parola Hatalı")
            return redirect('/account/login')
    return render(request, 'account/login.html', context)

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(form.cleaned_data.get('lastname'))
            print(form.cleaned_data.get('firstname'))
            newuser = User(
                        username=username,
                        first_name=form.cleaned_data.get('firstname'),
                        last_name=form.cleaned_data.get('lastname')
                       )
            newuser.set_password(password)
            newuser.save()
            newaccount = Account(
                        user=newuser,
                        twitter=None,
                        address=form.cleaned_data.get('address'),
                        city=form.cleaned_data.get('city'),
                        country=form.cleaned_data.get('country'),
                        postalcode=form.cleaned_data.get('postalcode'),
                        about=form.cleaned_data.get('about')
                        )
            newaccount.save()
            messages.success(request, 'Kayıt Başarılı')
            return redirect('/account/register')
        else:
            messages.warning(request, 'Parolalar Eşleşmiyor')
            return redirect('/account/register')
    context = {
        'form' : form
    }
    return render(request, 'account/register.html', context)