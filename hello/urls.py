from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.hello, name='hello-index'),
]