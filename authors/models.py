from tabnanny import verbose
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['name']

    def __str__(self):
        return self.name
