from django import forms

from class_based_views.models import Author, Book 


class AuthorForm(forms.ModelForm):

    class Meta: 
        model = Author 
        fields = '__all__'
    
class BookForm(forms.ModelForm):
     class Meta:
        model = Book
        fields = '__all__'