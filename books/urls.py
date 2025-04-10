from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('list/', views.BookListView.as_view(), name='book_list'),
    path('create/', views.BookCreateView.as_view(), name='create_book'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='update_book'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete_book'),
]
