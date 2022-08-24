from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title_bar': 'About Telemor',
        'title_page': ' About Telemor Hetan diak Liu',
        'kontributor': 'Diego Fernandes',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/contact', 'Contact'],
        ]
    }
    return render(request,'about/index.html', context)