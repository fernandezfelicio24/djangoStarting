from django.http import HttpResponse
from django.shortcuts import render

#import class based view
from django.views import View

#import Template View
from django.views.generic.base import TemplateView

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

# make class for parameter view
class ParameterView(TemplateView):
    template_name = 'parameterview.html'

    def get_context_data(self, *args, **kwargs):
        context = kwargs
        context['judul'] = "Home Parameter"
        context['writer'] = "Adasi Mau Rahun"
        return context

# make class for context view
class ContextView(TemplateView):

    template_name = 'context.html'

    def get_context_data(self):
        context = {
            'title' : 'Home Context',
            'writer' : 'Diego Gomes Fernandes'
        }

        return context