from django.contrib import admin
from django.urls import path
from amazon.books.views import authors_list
from amazon.books.views import (authors_detail, authors_new, authors_edit, authors_delete,
                                genres_new, genres_edit, genres_list, genres_delete, genres_detail,
                                index_view)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/new/', authors_new, name='authors-new'),
    path('authors/<int:id>/edit/', authors_edit, name='authors-edit'),
    path('authors/<int:id>/delete/', authors_delete, name='authors-delete'),
    path('authors/<int:pk>/', authors_detail,
            name='authors-detail'),
    path('authors/', authors_list,
            name='authors-list'),

    path('genres/', genres_list, name='genre-list'),
    path('genres/new/', genres_new, name='genre-new'),
    path('genres/<int:id>/', genres_detail, name='genre-detail'),
    path('genres/<int:id>/edit/', genres_edit, name='genre-edit'),
    path('genres/<int:id>/delete/', genres_delete, name='genre-delete'),

    path('', index_view, name='index')
]
