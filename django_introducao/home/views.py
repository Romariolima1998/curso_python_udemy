from django.shortcuts import render

# Create your views here.


def home(request):
    print('Blog')
    return render(
        request,
        'home/index.html'
    )
