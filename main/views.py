from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Безорфографичный предупреждал осталось пор диких. Рекламных ее предложения до бросил текст. Взгляд, рыбными над.'
    }

    return render(request, 'main/about.html', context)