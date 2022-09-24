from django.contrib import admin
from . models import AuthorGender, Gender
#from . models import AuthorGender
# Register your models here.

class GenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)


admin.site.register(Gender,GenderAdmin)
admin.site.register(AuthorGender)

