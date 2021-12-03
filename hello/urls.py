from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.hello, name='hello-index'),
    path('view/<str:pk>/', views.hello_view, name='hello-view'),
    path('delete/<str:pk>/', views.hello_delete, name='hello-delete'),
    path('add/', views.hello_add, name='hello-add'),
    path('update/<str:pk>/', views.hello_update, name='hello-update'),
]