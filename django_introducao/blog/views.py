from django.shortcuts import render

# Create your views here.


def blog(request):
    print('Blog')
    return render(
        request,
        'blog/index.html'
    )
