from django.contrib import admin

from class_based_views.models import Author, Book

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)