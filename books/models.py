from tabnanny import verbose
from venv import create
from django.db import models
from authors.models import Author
# Create your models here.


# Relación uno a muchos con autores
class Book(models.Model):
    title = models.CharField(max_length=50)
    # Un libro le pertenece a un autor: relación uno a muchos
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    pages = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'
        ordering = ['-created_at']

    def __str__(self):
        return self.title



