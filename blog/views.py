from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

#import model
from .models import Post

#Import form here
from .forms import PostForm

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

def create(request):

    blog_form = PostForm()

    context = {
        'blog_form' : blog_form
    }
    return render(request, 'blog/createblog.html', context)

def store(request):

    blog_form = PostForm(request.POST or None)
    error = None

    if request.method == 'POST':

        if blog_form.is_valid():
            # Post.objects.create(
            #     title = blog_form.cleaned_data.get('title'),
            #     body=blog_form.cleaned_data.get('body'),
            #     email=blog_form.cleaned_data.get('email'),
            #     adress=blog_form.cleaned_data.get('address'),
            #     category=blog_form.cleaned_data.get('category'),
            # )
            blog_form.save()

            return redirect("/blog")
        else:
            error = blog_form.errors

    context = {
        'blog_form': blog_form,
        'error': error
    }
    return render(request,'blog/createblog.html', context)


def show(request):
    pass

def edit(request, edit_id):

    edit_obj = Post.objects.get(id=edit_id)

    data = {
        'id': edit_obj.id,
        'title': edit_obj.title,
        'body': edit_obj.body,
        'email': edit_obj.email,
        'adress': edit_obj.adress,
        'category': edit_obj.category,
    }
    #print(data)
    blog_form = PostForm(request.POST or None, initial=data, instance=edit_obj)

    context = {
        'blog_form': blog_form,
        'id_blog' : edit_id,
    }

    return render(request,'blog/editblog.html', context)

def update(request, update_id):
    #return HttpResponse('<h1>Coba UPDATE</h1>')
    edit_obj = Post.objects.get(id=update_id)
    error = None
    print(edit_obj)
    data = {
        'title': edit_obj.title,
        'body': edit_obj.body,
        'email': edit_obj.email,
        'adress': edit_obj.adress,
        'category': edit_obj.category,
    }
    blog_form = PostForm(request.POST or None, initial=data, instance=edit_obj)

    if request.method == 'POST':

        if blog_form.is_valid():

            blog_form.save()

            return redirect("/blog")
        else:
            error = blog_form.errors

    context = {
        'blog_form': blog_form,
        'error': error
    }
    return render(request, 'blog/editblog.html', context)

def destroy(request, delete_id):

    Post.objects.filter(id=delete_id).delete()

    return redirect("/blog")


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

# bellow is the function of CRUD of blog but with new way call Clas Based View

from django.views.generic.base import TemplateView, RedirectView, View


class BlogSubList:

    def get_list_data(self, get_request):
        if len(get_request) == 0:
            sublist = Post.objects.all()
        elif get_request.__contains__('content_filter'):
            sublist = Post.objects.filter(category = get_request['content_filter'])
        else:
            sublist = Post.objects.none()
        return sublist

class BlogListView(BlogSubList, TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, *args, **kwargs):
        #posts = Post.objects.all()
        posts = self.get_list_data(self.request.GET)

        list_categories  = Post.objects.values_list('category', flat=True).distinct()
        print(list_categories)
        #list_categories = Post.objects.values('category').distinct()

        context = {
            'Posts': posts,
            'data_category' : list_categories,
            'page_title' : 'This is the list of Blog using Class-based view '
        }

        return context

class BlogDeleteView(RedirectView):
    pattern_name = 'blog:index'
    #permanent = False
    #query_string = False

    def get_redirect_url(self, *args, **kwargs):
        delete_id = kwargs['delete_id']
        Post.objects.filter(id=delete_id).delete()

        return super().get_redirect_url()


class BlogFormView(View):

    template_name = 'blog/createblog.html'
    form = PostForm()
    mode = None
    context = {}

    def get(self, *args, **kwargs):

        if self.mode == 'update':
            edit_obj = Post.objects.get(id=kwargs['update_id'])
            data = edit_obj.__dict__
            print(data)
            self.form = PostForm(initial=data, instance=edit_obj)

        self.context = {
            'blog_form': self.form
        }

        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):

        if kwargs.__contains__('update_id'):
            edit_obj = Post.objects.get(id=kwargs['update_id'])
            self.form = PostForm(self.request.POST, instance=edit_obj)
        else:
            self.form = PostForm(self.request.POST)

        if self.form.is_valid():
            self.form.save()

        return redirect('blog:index')