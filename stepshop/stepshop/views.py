from django.shortcuts import render


def index(request):
    title = 'Главная сттаница'

    context = {
        'title': title,
    }
    return render(request, 'index.html', context)



def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contact.html')
