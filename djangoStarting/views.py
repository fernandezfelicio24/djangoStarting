from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title_bar' : 'Telemor',
        'title_page' : 'Telemor Hetan diak Liu',
        'kontributor' : 'Felicio Fernandez',
        'banner' : 'img/banner_home.png',
        'nav': [

            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/contact', 'Contact'],
        ]
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')