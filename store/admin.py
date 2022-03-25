from django.contrib import admin
from . models import Genre, Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = ['is_available']
    prepopulated_fields =  {'slug' : ('title',)}
    

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields =  {'slug' : ('name',)}
    
    
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)