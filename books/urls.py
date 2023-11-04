from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('search/', views.book_search, name='book_search'),
    path('filter/', views.book_filter, name='book_filter'),
]