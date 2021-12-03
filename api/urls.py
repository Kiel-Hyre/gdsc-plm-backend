from django.urls import path
from . import views

urlpatterns = [
    # path('list/', views.api, name='api-index'),
    path('list/', views.APIListView.as_view(), name='api-index'),
    # path('view/<str:pk>/', views.api_view, name='api-view'),
    path('view/<str:pk>/', views.APIGetView.as_view(), name='api-view'),
    path('delete/<str:pk>/', views.APIDeleteView.as_view(), name='api-delete'),
    path('add/', views.APICreateView.as_view(), name='api-add'),
    path('update/<str:pk>/', views.APIUpdateView.as_view(), name='api-update'),
]