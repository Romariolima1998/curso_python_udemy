
from django.urls import path
from home import views


# http request<> http response

urlpatterns = [
    path('', views.home),
]
