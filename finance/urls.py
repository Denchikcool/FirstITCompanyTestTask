from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transactions'),
    path('create/', views.transaction_create, name='create'),
    path('edit/<int:pk>/', views.transaction_update, name='edit'),
    path('delete/<int:pk>/', views.transaction_delete, name='delete')
]