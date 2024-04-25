from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection

from .forms import CustomUserCreationForm
from .models import Article
from django.contrib.auth.forms import UserCreationForm
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def handlerReg(request):
    if request.method == 'POST':
        name = (request.POST.get("name"))
        email = (request.POST.get("email"))
        password = (request.POST.get("pass"))
        cursor = connection.cursor()
        values = (name, email, password)
        cursor.execute("INSERT INTO users (name, email, pass) VALUES (%s, %s, %s)", values)
        connection.commit()
        return HttpResponse("OK!")
    else:
        return render(request, 'reg.html')

def handlerLogin(request):
    if request.method == 'POST':
        email = (request.POST.get("email"))
        password = (request.POST.get("pass"))
        cursor = connection.cursor()
        values = (email, password)
        cursor.execute("SELECT * FROM users WHERE email=%s AND pass=%s ", values)
        row = cursor.fetchone()
        # request.session['id'] = row[0]
        # request.session['name'] = row[1]
        # request.session['email'] = row[2]
        return HttpResponse("OK!")
    else:
        return render(request, 'login.html')

def showProfile(request):
    return HttpResponse("request.session['name']")

def addArticle(request):
    # ДЗ: получите данные из формы и запишите их в базу данных
    return render(request, 'addArticle.html')

def editArticle():
    pass

def singleArticle(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'singleArticle.html', {'article': article})
def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})