from tabnanny import verbose
from django.db import models

from books.models import Book
from authors.models import Author
# Create your models here.

class Gender(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book,related_name='books')
    authors = models.ManyToManyField(Author, through='AuthorGender')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'
        ordering = ['name']

    def __str__(self):
        return self.name

    
class AuthorGender(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name        = 'AuthorGender'
        verbose_name_plural = 'AuthorGenders'
        ordering = ['gender']


    def __str__(self):
        return str(self.gender)
