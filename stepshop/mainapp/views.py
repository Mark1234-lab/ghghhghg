from django.shortcuts import render

from mainapp.models import Product, ProductKategory

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]


def products(request):
    title = 'Продукты'

    products_ = Product.objects.all()
    categories = ProductKategory.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_,
        'categories': categories,
    }
    return render(request, 'products.html', context)


def product(request):
    return render(request, 'product.html')
