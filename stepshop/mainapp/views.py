from django.shortcuts import render


def products(request):
    title = 'Продукты'

    context = {
        'title': title,
    }
    return render(request, 'products.html')


def product(request):
    return render(request, 'product.html')
