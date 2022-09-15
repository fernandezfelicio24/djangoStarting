from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import About

# Import form here
from .forms import ContactForm

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
        # 'nav': [
        #     ['/', 'Home'],
        #     ['/blog', 'Blog'],
        # ]
    }
    return render(request,'about/index.html', context)


def handle_id(request, id=None):

    #QUERY SET
    abouts = About.objects.all()
    about_obj = None
    #if we use this the result will be server error
    #about_obj = About.objects.get(id=id)

    #if we use this the result will be not found
    about_obj = get_object_or_404(About, id=id)

    if about_obj is not None:
        context = {
            'title_bar': 'About Telemor',
            'title_page': ' About Telemor Hetan diak Liu',
            'kontributor': 'Diego Fernandes',
            'app_css': 'about/css/styles.css',
            'about': abouts,
            'object': about_obj,
            'nav': [
                ['/', 'Home'],
                ['/blog', 'Blog'],
            ]
        }
        return render(request, 'about/index.html', context)

def companyprf(request):

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
    return HttpResponse('<h1>Welcome ! Testing URL name space, Company Profile </h1>')


def companmsn(request):

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
    return HttpResponse('<h1>Welcome ! Testing URL name space, Company Mission </h1>')


def companyvsn(request):

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
    return HttpResponse('<h1>Welcome ! Testing URL name space, Company Vision </h1>')



def aboutsps(request, input):

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
    return HttpResponse('<h1>Welcome ! Testing URL name space,  </h1>'+ input)

def aboutform(request):

    contact_form = ContactForm()

    context = {
        'contact_form' : contact_form
    }
    if request.method == 'POST':
        context['name'] = request.POST['name']
        context['gender'] = request.POST['gender']
        context['address'] = request.POST['address']
        context['date_birth'] = request.POST['date_birth']
        context['pos_code'] = request.POST['pos_code']
        context['city'] = request.POST['city']
        context['province'] = request.POST['province']
        context['agree'] = request.POST['agree_or_not']
    else:
        print("This is GET Method")
    #test if get the data or not
    print(request.POST)
    return render(request, 'about/aboutForm.html', context)



