from django.shortcuts import render


def platform(request):
    pagename = 'Главная страница'
    content = ''
    context = {
        'pagename': pagename,
        'content': content
    }
    return render(request, 'fourth_task/platform.html', context)


def games(request):
    pagename = 'Магазин'
    content = ['Atomic Heart', 'Cyberpunk 2077', 'Payday 2']
    context = {
        'content': content,
        'pagename': pagename
               }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    pagename = 'Корзина'
    content = 'Ваша корзина пуста'
    context = {
        'pagename': pagename,
        'content': content
    }
    return render(request, 'fourth_task/cart.html', context)
