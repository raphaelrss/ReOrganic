from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def trocas(request):
    return render(request, 'trocas.html')


def minhas_trocas(request):
    return render(request, 'minhas_trocas.html')


def notifications(request):
    return render(request, 'notifications.html')


def posts(request):
    return render(request, 'posts.html')


def faq(request):
    return render(request, 'faq.html')


