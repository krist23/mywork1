from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from mymarks.models import Students
from django.contrib import messages


def main(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/authed')
        return render(request, 'main.html')


def loginp(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/authed')
        else:
            return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            messages.error(request, 'Заполните все поля')
            return redirect('/login')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/authed')
        else:
            messages.error(request, 'Неправильный логин или пароль!')
            return redirect('/login')


def registerp(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/authed')
        else:
            return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        mail = request.POST.get('mail', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if username == '' or password1 == '' or password2 == '':
            messages.error(request, 'Не все поля заполнены')
            return redirect('/register')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Ник уже занят')
            return redirect('/register')
        elif len(username) < 3:
            messages.error(request, 'Слишком короткий ник')
            return redirect('/register')
        elif len(username) > 20:
            messages.error(request, 'Слишком длинный ник')
            return redirect('/register')
        elif len(password1) < 6:
            messages.error(request, 'Слишком короткий пароль')
            return redirect('/register')
        elif len(password1) > 50:
            messages.error(request, 'Слишком длинный пароль')
            return redirect('/register')
        elif password1 != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('/register')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password1, first_name=name)
            user.save()
            login(request, user)
            return redirect('/authed')


def authed(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            user = request.user.username
            marks = mark.objects.filter(author=request.user)

            parms = {'username': request.user.username,
                     'user': request.user.first_name, 'marks': marks}
            return render(request, 'authed.html', parms)
    else:
        return redirect('/')


def logoutp(request):
    if request.method == 'GET':
        logout(request)
    return redirect('/')


def addmark(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'addmark.html')
        if request.method == 'POST':
            sub = request.POST.get('subject', '')
            mar = request.POST.get('mark', '')
            des = request.POST.get('description', '')

            Mark = mark()
            Mark.author = request.user
            Mark.subject = sub
            Mark.value = mar
            Mark.description = des
            Mark.save()
            return redirect('/')
    else:
        return redirect('/')
