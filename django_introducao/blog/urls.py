
from django.urls import path
from blog import views

# http request<> http response

urlpatterns = [
    path('', views.blog)
]
