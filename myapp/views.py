from django.shortcuts import render


def menu_page(request, url):
    context = {
        'menu_name': url,
        'current_path': request.path.split("/")[-2]  # передаем текущий URL в контекст
    }
    return render(request, 'myapp/menu_page.html', context)

def index(request):
    context = {'menu_name': 'all'}
    return render(request, 'myapp/menu_page.html', context)
