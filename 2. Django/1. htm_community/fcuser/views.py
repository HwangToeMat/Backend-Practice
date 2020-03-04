from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm
# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        useremail = request.POST.get('useremail', None)

        res_data = {}

        if not (username and password and re_password and useremail):
            res_data['error'] = '모든값을 입력하세요!'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다!'
        else:
            fcuser = Fcuser(
                username=username,
                password=make_password(password),
                useremail=useremail
            )
            fcuser.save()
        return render(request, 'register.html', res_data)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')
