from django.contrib import admin
from . models import Genre, Book, Author, Publisher

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = ['is_available']
    prepopulated_fields =  {'slug' : ('title',)}
    

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields =  {'slug' : ('name',)}
    
    
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields =  {'slug' : ('name',)}
    
    
class PublisherAdmin(admin.ModelAdmin):
    prepopulated_fields =  {'slug' : ('name',)}
    
    
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)