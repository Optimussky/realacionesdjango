from tabnanny import verbose
from django.db import models

from authors.models import Author

# Relación uno a uno con author

class Profile(models.Model):
    alias       = models.CharField(max_length=50)
    # Un Author puede existir sin un perfil, PERO un PERFIL no  puede existir sin un Author
    # Por lo tanto podemos usar OneToOneField en author
    author      = models.OneToOneField(Author, on_delete=models.CASCADE, default=None)
    created_at  = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering     = ['alias']


    def __str__(self):
        return self.alias