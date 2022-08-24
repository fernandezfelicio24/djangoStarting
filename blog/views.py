from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'title_bar': 'Telemor Blog',
        'title_page': 'Telemor nia Blog diaria',
        'kontributor': 'vtl_it_felicio',
        'app_css':'blog/css/styles.css',
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/contact', 'Contact'],
            ['/blog/story', 'Story'],
            ['/blog/news', 'News'],
        ]
    }
    #return HttpResponse('<h1>Ini adalah recent post</h1>')
    return render(request, 'blog/index.html', context)


def story(request):
    context = {
        'title_bar': 'Telemor Story',
        'title_page': 'Telemor Story Around',
        'kontributor': 'vtl_it_ajito'
    }
    return render(request,  'blog/index.html', context)
    #return HttpResponse('<h1>Ini adalah recent post</h1>')

def news(request):
    context = {
        'title_bar': 'Telemor News',
        'title_page': 'Telemor News everywhere',
        'kontributor': 'vtl_it_ricardo'
    }
    return render(request, 'blog/index.html', context)
    #return HttpResponse('<h1>Ini adalah recent post</h1>')

def recent(request):

    return HttpResponse('<h1>Ini adalah recent post</h1>')
