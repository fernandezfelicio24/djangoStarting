from django.http import HttpResponse
from django.shortcuts import render

#import class based view
from django.views import View


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

def testform(request):
    context = {

    }
    if request.method == 'POST':
        context['name'] = request.POST['name']
        context['adress'] = request.POST['adress']
    else:
        print("This is GET Method")

    return render(request, 'testForm.html', context)


def about(request):
    return render(request, 'about.html')

def testbase(request):

    context = {
        'info1': 'Learning class based view',
    }

    if request.method == 'POST':
        context['info1'] = 'POST FUNCTION based'

    return render(request, 'testbase1.html', context)

class IndexClassView(View):

    #template_name = 'testbase1.html'
    template_name = ''
    context = {

    }
    #override method get from parent class View
    def get(self, request):
        self.context['info1'] = 'GET FUNCTION based'
        return render(request, self.template_name,self.context)

    def post(self, request):
        self.context['info1'] = 'POST FUNCTION based'
        return render(request, self.template_name, self.context)