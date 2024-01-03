from django.shortcuts import render
from django.http import Http404
from blog.data import posts

# Create your views here.
context = {
    'title': 'blog - ',
    'text': 'meu blog',
    'posts': posts,
}


def blog(request):
    print('blog')
    return render(
        request,
        'blog/blog.html',
        context,
    )


def post(request, id):
    print('post')
    postblog = None

    for p in posts:
        if p['id'] == id:
            postblog = p
            break
    
    if postblog is None:
        raise Http404('post nao existe')
    
    context = {
        'title': postblog['title'] + ' - ',
        'text': 'meu post',
        'post': postblog,
    }

    return render(
        request,
        'blog/post.html',
        context,
    )
