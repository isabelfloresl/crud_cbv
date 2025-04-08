"""
URL configuration for crud_cbv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from class_based_views.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/new/', AuthorCreateView.as_view(), name='author_create'),
    path('update-author/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('delete-author/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),
    
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),

    path('search/', SearchView.as_view(), name='search'),

]
