from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Post

def index(request):
    # QUERY SET
    posts = Post.objects.all()
    #print(posts)
    categories = Post.objects.values('category').distinct()
    context = {
        'title_bar': 'Telemor Blog',
        'title_page': 'Telemor nia Blog diaria',
        'kontributor': 'vtl_it_reinaldo',
        'app_css':'blog/css/styles.css',
        'Kategories': categories,
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

def categoryPost(request, categoryInput):
    post = Post.objects.filter(category=categoryInput)

    print(post)
    return HttpResponse("category post")


def singlePost(request, slugInput):
    post = Post.objects.get(slug=slugInput)

    judul = "<h1>{}</h1>".format(post.title)
    body = "<p>{}</p>".format(post.body)
    category = "<p> {} </p>".format(post.category)
    return HttpResponse(judul + body + category)

def categoryPostingan(request, categoryInput):

    posts = Post.objects.filter(category=categoryInput)
    print(categoryInput)
    categories = Post.objects.values('category').distinct()

    print(categories)

    context = {

        'title_page': 'Showing based on Category',
        'kontributor': 'el_chino antrax',
        'Kategories': categories,
        'Posts': posts,
        # 'nav': [
        #     ['/', 'Home'],
        #     ['/about', 'About'],
        #     ['/blog', 'Blog'],
        # ]
    }
    return render(request, 'blog/categoryblog.html', context)
    #return HttpResponse(posts.category + posts.body  )

def detailPost(request, slugInput):

    posts = Post.objects.get(slug=slugInput)

    context = {

        'title_page': 'DETAIL POST',
        'kontributor': 'el_chino antrax',
        'Posts': posts,
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog'],
        ]
    }
    return render(request, 'blog/detailBlog.html', context)
