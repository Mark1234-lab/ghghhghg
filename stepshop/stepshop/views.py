from django.shortcuts import render

from mainapp.models import Product, ProductKategory

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]

def index(request):
    title = 'Главная страница'

    products_ = Product.objects.all()
    categories_ = ProductKategory.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'index.html', context)



def about(request):
    title = 'О нас'

    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'about.html', context)


def contacts(request):
    title = 'Контакты'

    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'contact.html', context)
