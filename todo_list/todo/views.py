from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'todo/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'todo/about.html', {'title': 'О сайте'})
