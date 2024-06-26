from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserFormRegister, OrderPenjualan
from django.contrib import messages
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from sales.models import *

def dictfetchall(cursor):
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username atau Password anda salah')

        content = {}
        return render(request, 'login.html', content)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserFormRegister()

        if request.method == 'POST':
            form = UserFormRegister(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Akun ' + user + ' sudah dibuat')
                return redirect('login')

        content = {'form' : form}
        return render(request, 'register.html', content)

@login_required(login_url='login')
def tabel_penjualan(request):
    user_list = FaktaPenjualan.objects.all()
    hal = Paginator(user_list, 15)
    halaman = request.GET.get('page', 1)

    try:
        page = hal.page(halaman)
    except EmptyPage:
        page = hal.page(1)

    content = {
        'halaman' : page,

    }

    return render(request, 'tabel_penjualan.html', content)

@login_required(login_url='login')
def tabel_pengiriman(request):
    user_list = FaktaPengiriman.objects.all()
    hal = Paginator(user_list, 15)
    halaman = request.GET.get('page', 1)

    try:
        page = hal.page(halaman)
    except EmptyPage:
        page = hal.page(1)

    content = {
        'halaman' : page,
    }

    return render(request, 'tabel_pengiriman.html', content)

    


