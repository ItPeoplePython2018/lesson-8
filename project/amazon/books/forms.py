from django import forms
from amazon.books.models import Author, Genre


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'name': 'Имя автора'
        }


class AuthorDeleteForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('id', )


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        labels = {
            'name': 'Название'
        }


class GenreDeleteForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('id', )
