from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Post

def index(request):
    # QUERY SET
    posts = Post.objects.all()
    #print(posts)

    context = {
        'title_bar': 'Telemor Blog',
        'title_page': 'Telemor nia Blog diaria',
        'kontributor': 'vtl_it_reinaldo',
        'app_css':'blog/css/styles.css',
        'Posts' : posts,
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog/soccer', 'Soccer'],
            ['/blog/story', 'Story'],
            ['/blog/news', 'News'],
            ['/blog/jurnal', 'Jurnal'],
            ['/blog/gossip', 'Gossip'],
        ]
    }
    #return HttpResponse('<h1>Ini adalah recent post</h1>')
    return render(request, 'blog/index.html', context)

def soccer(request):
    # QUERY SET
    posts = Post.objects.filter(title='Soccer')
    # print(posts)

    context = {
        'title_bar': 'Soccer',
        'title_page': 'Everything about soccer',
        'kontributor': 'vtl_it_reinaldo',
        'app_css': 'blog/css/styles.css',
        'Posts': posts,
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog'],
        ]
    }

    return render(request, 'blog/categoryblog.html', context)

def news(request):
    # QUERY SET
    posts = Post.objects.filter(title='News')
    # print(posts)

    context = {
        'title_bar': 'Soccer',
        'title_page': 'Everything about News',
        'kontributor': 'vtl_it_tiago',
        'app_css': 'blog/css/styles.css',
        'Posts': posts,
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog'],
        ]
    }

    return render(request, 'blog/categoryblog.html', context)

def jurnal(request):
    posts = Post.objects.filter(title='Jurnal')

    context = {
        'title_bar': 'Telemor Story',
        'title_page': 'Telemor Jurnal',
        'kontributor': 'vtl_it_diego',
        'Posts': posts,
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog'],
        ]
    }
    return render(request,  'blog/categoryblog.html', context)
    #return HttpResponse('<h1>Ini adalah recent post</h1>')

def gossip(request):
    posts = Post.objects.filter(title='Gossip')

    context = {
        'title_bar': 'Telemor News',
        'title_page': 'Telemor News everywhere',
        'kontributor': 'vtl_it_adasi',
        'Posts': posts,
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog'],
        ]
    }
    return render(request, 'blog/categoryblog.html', context)
    #return HttpResponse('<h1>Ini adalah recent post</h1>')

