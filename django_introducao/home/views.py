from django.shortcuts import render


# Create your views here.
context = {
    'title': 'home - '
}

def home(request):
    print('home')
    return render(
        request,
        'home/index.html',
        context,
    )
