from django.contrib import admin
from . models import Genre, Book, Review

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = ['is_available']
    prepopulated_fields =  {'slug' : ('title',)}
    

admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(Review)