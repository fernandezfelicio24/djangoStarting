from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title_bar': 'About Telemor',
        'title_page': ' About Telemor Hetan diak Liu',
        'kontributor': 'Diego Fernandes',
        'app_css': 'about/css/styles.css',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
        ]
    }
    return render(request,'about/index.html', context)
