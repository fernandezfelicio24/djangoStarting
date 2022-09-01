from django.shortcuts import render

# Create your views here.
from .models import About
def index(request):

    #QUERY SET
    abouts = About.objects.all()
    print(abouts)

    context = {
        'title_bar': 'About Telemor',
        'title_page': ' About Telemor Hetan diak Liu',
        'kontributor': 'Diego Fernandes',
        'app_css': 'about/css/styles.css',
        'about' : abouts,
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
        ]
    }
    return render(request,'about/index.html', context)


def handle_id(request, id=None):

    #QUERY SET
    abouts = About.objects.all()
    about_obj = None
    if id is not None:
        about_obj = About.objects.get(id=id)
    context = {
        'title_bar': 'About Telemor',
        'title_page': ' About Telemor Hetan diak Liu',
        'kontributor': 'Diego Fernandes',
        'app_css': 'about/css/styles.css',
        'about' : abouts,
        'object' : about_obj,
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
        ]
    }
    return render(request,'about/index.html', context)
