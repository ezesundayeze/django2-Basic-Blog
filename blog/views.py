from django.shortcuts import render
from .models import post

def index(request):
    posts = post.objects.all()[:10]


    context = {
        'title':'Home Page',
        'posts':posts
    }
    return render(request, 'blog/index.html', context, )
    
def about(request, slug):

    posts = post.objects.get(slug=slug)

    context = {
        'mposts':posts
    }

    return render(request, 'blog/about.html', context)
