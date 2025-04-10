from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('list', views.AuthorListView.as_view(), name='author_list'),
    path('create/', views.AuthorCreateView.as_view(), name='create_author'),
    path('<int:pk>/update/', views.AuthorUpdateView.as_view(), name='update_author'),
    path('<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='delete_author'),
]
