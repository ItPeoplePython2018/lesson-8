from django.db import models


class Author(models.Model):
    name = models.CharField(verbose_name='Имя',
                            max_length=100)
    lastname = models.CharField(verbose_name='Фамилия',
                                max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.lastname}'

    @property
    def full_name(self):
        return f'{self.name} {self.lastname}'


class Genre(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(Author, null=True,
        related_name='books', on_delete=models.SET_NULL)

    genres = models.ManyToManyField(Genre,
     related_name='books')

    rate = models.FloatField()

    def __str__(self):
        return f'{self.title} :: {self.author} [{self.rate}]'
