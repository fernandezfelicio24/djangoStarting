from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title_bar' : 'Kelas Terbuka',
        'title_page' : 'Never Stop Learning',
        'kontributor' : 'Felicio Fernandez',
        'banner' : 'img/banner_home.png',
        # 'nav': [
        #     ['/blog', 'Blog'],
        #     ['/about', 'About'],
        # ]
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')