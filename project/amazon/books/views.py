from django.shortcuts import render, redirect, get_object_or_404
from amazon.books.models import Author, Book, Genre
from django.views.generic import DetailView, TemplateView

from amazon.books.forms import AuthorForm, AuthorDeleteForm, GenreForm, GenreDeleteForm

class AuthorDetail(DetailView):
    model = Author
    template_name = 'author_detail.html'

authors_detail = AuthorDetail.as_view()


class IndexView(TemplateView):
    template_name = 'index.html'

index_view = IndexView.as_view()


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {
        'object_list': authors
    })


def authors_new(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('authors-detail', pk=author.id)
    else:
        form = AuthorForm()
    return render(request, 'author_new.html', {
        'form': form
    })


def authors_edit(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save()
            return redirect('authors-detail', pk=author.id)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_new.html', {
        'form': form
    })


def authors_delete(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        form = AuthorDeleteForm(request.POST, instance=author)
        if form.is_valid():
            author.delete()
            return redirect('authors-list')
    else:
        form = AuthorDeleteForm(instance=author)
    return render(request, 'author_delete.html', {
        'form': form
    })


def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre.html', {
        'genres': genres
    })


def genres_new(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre-list')
    else:
        form = GenreForm()
    return render(request, 'genre_new.html', {
        'form': form
    })


def genres_edit(request, id):
    genre = get_object_or_404(Genre, id=id)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre-list')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'genre_new.html', {
        'form': form
    })


def genres_delete(request, id):
    genre = get_object_or_404(Genre, id=id)
    if request.method == 'POST':
        form = GenreDeleteForm(request.POST, instance=genre)
        if form.is_valid():
            genre.delete()
            return redirect('genre-list')
    else:
        form = GenreDeleteForm(instance=genre)
        return render(request, 'genre_delete.html', {
            'form': form
        })


def genres_detail(request, id):
    genre = get_object_or_404(Genre, id=id)
    return render(request, 'genre_detail.html', {
        'genre': genre
    })
